from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, FormView, DeleteView, UpdateView, CreateView, RedirectView
from django.contrib.auth.decorators import login_required

from study_calendar.models import TimeTable, Cell

from study_calendar.forms import NewTimeTableForm, EditTimeTableForm
from comments.forms import CreateCommentForm
from django.core import serializers
import json


@method_decorator(login_required, name='dispatch')
class TimeTableView(DetailView):
    template_name = "TimeTable.html"
    model = TimeTable

    pk_url_kwarg = "timetable"
    context_object_name = "timetable"


@method_decorator(login_required, name='dispatch')
class TimeTableListView(ListView, FormView):
    template_name = "TimeTableList.html"
    model = TimeTable
    context_object_name = 'timetables'
    form_class = NewTimeTableForm
    success_url = reverse_lazy("calendar:list")

    def get_queryset(self):
        query_set = TimeTable.objects
        if self.request.GET.get("section") == "my":
            query_set = self.request.user.timetables
        search_field = self.request.GET.get("search", "")
        query_set = query_set.filter(name__contains=search_field)
        return query_set.all()

    def form_valid(self, form):
        timetable = form.save(commit=False)
        timetable.owner = self.request.user
        timetable.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["edit_form"] = EditTimeTableForm
        context["use_search"] = True
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # form.fields["study_group"].choices = self.request.user.studyGroup.all().values_list()
        return form


@method_decorator(login_required, name='dispatch')
class TimeTableDeleteView(DeleteView):
    model = TimeTable
    success_url = reverse_lazy("calendar:list")
    pk_url_kwarg = "timetable"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise Http404
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponse()

    def get(self, request, *args, **kwargs):
        return HttpResponse()


@method_decorator(login_required, name='dispatch')
class TimeTableEditView(UpdateView):
    model = TimeTable
    success_url = reverse_lazy("calendar:list")
    pk_url_kwarg = "timetable"
    form_class = EditTimeTableForm
    template_name = "form_view.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise Http404
        return obj


    def form_valid(self, form):
        self.model = form.save()
        return HttpResponse()


@method_decorator(login_required, name='dispatch')
class TimeTableSubscribeView(RedirectView):

    def get(self, request, *args, **kwargs):
        timetable = get_object_or_404(TimeTable, pk=kwargs["timetable"])
        request.user.timetables.add(timetable)
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse("calendar:list")


@method_decorator(login_required, name='dispatch')
class CellDetailView(DetailView, FormView):
    template_name = "DetailsCell.html"
    #pk_url_kwarg = "cell"
    model = Cell
    form_class = CreateCommentForm

    def get_object(self, queryset=None):
        timetable = get_object_or_404(TimeTable, pk=self.kwargs.get("timetable", 0))
        cell = timetable.cell_set.filter(pk=self.kwargs.get("cell")).get()
        if cell is None:
            raise Http404()
        return cell


@method_decorator(login_required, name='dispatch')
class CellCreateView(CreateView):
    template_name = "CellCreateView.html"
    model = Cell
    fields = ['teacher', 'subject', 'timeOfStart', 'timeOfEnd', 'dateOfStart', 'dateOfEnd', 'dayOfWeek']

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request, "timetable_obj"):
            timetable = get_object_or_404(TimeTable, pk=kwargs["timetable"])
            if timetable.owner != request.user:
                raise Http404
            request.timetable_obj = timetable
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            cell = form.save(commit=False)
            cell.table = request.timetable_obj
            cell.save()
            return redirect("calendar:timetable", timetable=request.timetable_obj.pk)
        return self.get(request, *args, **kwargs)
