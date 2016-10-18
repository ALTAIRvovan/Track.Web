from django.shortcuts import render

# Create your views here.
from django.views.generic import RedirectView


class HomePageView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        return "/timetable"
