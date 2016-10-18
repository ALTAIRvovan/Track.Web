from django.contrib import admin

# Register your models1 here.
#вынести в admin.py
from study_calendar.models.Cell import Cell
from study_calendar.models.StudyGroup import StudyGroup
from study_calendar.models.Teacher import Teacher
from study_calendar.models.TimeTable import TimeTable

admin.site.register(Cell)
admin.site.register(StudyGroup)
admin.site.register(Teacher)
admin.site.register(TimeTable)
