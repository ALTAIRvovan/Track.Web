from django.contrib import admin

from study_calendar.models import Cell
from study_calendar.models import Teacher
from study_calendar.models import TimeTable

admin.site.register(Cell)
admin.site.register(Teacher)
admin.site.register(TimeTable)
