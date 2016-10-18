from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView

from study_calendar.models.TimeTable import TimeTable
from study_calendar.models.Cell import Cell


class TimeTableView(DetailView):
    template_name = "TimeTable.html"
    model = TimeTable

    pk_url_kwarg = "timetable"
    context_object_name = "timetable"


class TimeTableListView(ListView):
    template_name = "TimeTableList.html"
    model = TimeTable
    context_object_name = 'timetables'


class CellDetailView(DetailView):
    template_name = "DetailsCell.html"
    model = Cell

    def get(self, request, *args, **kwargs):
        timetable = TimeTable.objects.get(pk=kwargs["timetable"])
        cell = timetable.cell_set.filter(pk=kwargs["cell"]).get()
        return render(request, self.template_name, {'cell': cell})



