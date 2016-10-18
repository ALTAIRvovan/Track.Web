from django.db import models

#from study_calendar.models.TimeTable import TimeTable


class Cell(models.Model):

    table = models.ForeignKey('TimeTable')
    teacher = models.ForeignKey('Teacher')
    subject = models.CharField(max_length=255)
    timeOfStart = models.TimeField()
    timeOfEnd = models.TimeField()
    dateOfStart = models.DateField()
    dateOfEnd = models.DateField()
    dayOfWeek = models.IntegerField() #засунуть чейсес

    def getStartTime(self):
        return self.timeOfStart.strftime("%s")

    def getHowLong(self):
        return int(self.timeOfEnd.strftime("%s")) - int(self.timeOfStart.strftime("%s")) / 3600

    def __str__(self):
        return self.table.name + " " + str(self.dayOfWeek) + " " + str(self.timeOfStart)



