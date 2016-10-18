from django.contrib import admin

# Register your models1 here.
#вынести в admin.py
from study_calendar.models import Cell, StudyGroup, Teacher, TimeTable

admin.site.register(Cell)
admin.site.register(StudyGroup)
admin.site.register(Teacher)
admin.site.register(TimeTable)