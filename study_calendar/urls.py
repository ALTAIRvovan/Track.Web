from django.conf.urls import include, url

from study_calendar.views import TimeTableListView, TimeTableView, CellDetailView, TimeTableDeleteView, \
    TimeTableEditView, CellCreateView, TimeTableSubscribeView

urlpatterns = [
    url(r'^$', TimeTableListView.as_view()),
    url(r'^list$', TimeTableListView.as_view(), name="list"),
    url(r'^(?P<timetable>[0-9]+)/$', TimeTableView.as_view(), name="timetable"),
    url(r'^(?P<timetable>[0-9]+)/delete$', TimeTableDeleteView.as_view(), name="timetable.remove"),
    url(r'^(?P<timetable>[0-9]+)/edit$', TimeTableEditView.as_view(), name="timetable.edit"),
    url(r'^(?P<timetable>[0-9]+)/subscribe$', TimeTableSubscribeView.as_view(), name="timetable.subscribe"),
    url(r'^(?P<timetable>[0-9]+)/cell/(?P<cell>[0-9]+)$', CellDetailView.as_view(), name='cell_detail'),
    url(r'^(?P<timetable>[0-9]+)/cell/create$', CellCreateView.as_view(), name='cell.create'),
]

