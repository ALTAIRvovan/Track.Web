from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.views.generic import DetailView

from study_calendar.models.TimeTable import TimeTable


class HomePageView(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        return "/timetable"


class TimeTableView(DetailView):
    template_name = "TimeTable.html"
    model = TimeTable

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'timetable': TimeTable.objects.get(pk=1)})

class CellView(TemplateView):
    template_name = "Cell.html"