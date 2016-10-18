"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from study_calendar.views import *

urlpatterns = [
    url(r'^$', HomePageView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^timetable/list$', TimeTableListView.as_view()),
    url(r'^timetable/$', TimeTableView.as_view()),
    url(r'^timetable/(?P<timetable>[0-9]+)$', TimeTableView.as_view()),
    url(r'^timetable/(?P<timetable>[0-9]+)/cell/(?P<cell>[0-9])$', CellDetailView.as_view(), name='cell_detail'),
]
