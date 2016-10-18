from django.contrib import admin
from django.db import models

from study_calendar.models import TimeTable


class Cell(models.Model):

    table = models.ForeignKey('TimeTable')
    teacher = models.ForeignKey('Teacher')
    subject = models.CharField(max_length=255)
    timeOfStart = models.TimeField()
    timeOfEnd = models.TimeField()
    dateOfStart = models.DateField()
    dateOfEnd = models.DateField()
    dayOfWeek = models.IntegerField()

    def getStartTime(self):
        return self.timeOfStart.strftime("%s")




admin.site.register(Cell)
