from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, RedirectView

from study_calendar.models import Cell
from .forms import CreateCommentForm


# Create your views here.

class CreateCommentView(FormView, RedirectView):
    form_class = CreateCommentForm
    template_name = "CommentDetailView.html"

    def get_success_url(self):
        return reverse_lazy("calendar:cell_detail",
                            kwargs={"timetable": self.kwargs.get("timetable"), "cell": self.kwargs.get("cell")})

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.cell = get_object_or_404(Cell, pk=kwargs.pop("cell"))
            comment.save()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.cell = get_object_or_404(Cell, pk=self.kwargs.pop("cell"))
        comment.save()
        return render(self.request, "CommentDetailView.html", context={"comment":comment})



