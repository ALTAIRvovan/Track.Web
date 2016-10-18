from django.db import models

#from study_calendar.models import StudyGroup

class TimeTable(models.Model):


    name = models.CharField(max_length=255, blank=False, default='main')
    owner_group = models.ForeignKey('StudyGroup')

    #class Meta

    def __str__(self):
        return self.owner_group.name + " " + self.name

    def getCellsInDay(self):
        return self.cell_set.order_by('dayOfWeek')

