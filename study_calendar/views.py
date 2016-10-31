from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, FormView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required

from study_calendar.models import TimeTable
from study_calendar.models import Cell

from study_calendar.forms import NewTimeTableForm, EditTimeTableForm

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

    def post(self, request, *args, **kwargs):
        form = NewTimeTableForm(request.POST)
        if form.is_valid():
            timetable = form.save(commit=False)
            timetable.owner = request.user
            timetable.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["edit_form"] = EditTimeTableForm
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        #form.fields["study_group"].choices = self.request.user.studyGroup.all().values_list()
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

    def get(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TimeTableEditView(UpdateView):
    model = TimeTable
    success_url = reverse_lazy("calendar:list")
    pk_url_kwarg = "timetable"
    form_class = EditTimeTableForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise Http404
        return obj


@method_decorator(login_required, name='dispatch')
class CellDetailView(DetailView):
    template_name = "DetailsCell.html"
    model = Cell

    def get(self, request, *args, **kwargs):
        timetable = TimeTable.objects.get(pk=kwargs["timetable"])
        cell = timetable.cell_set.filter(pk=kwargs["cell"]).get()
        return render(request, self.template_name, {'cell': cell})
