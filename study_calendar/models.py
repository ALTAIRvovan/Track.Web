from django.db import models

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
        return self.timeOfStart.hour * 60 + self.timeOfStart.minute

    def getHowLong(self):
        return (self.timeOfEnd.hour - self.timeOfStart.hour) * 60 + \
               self.timeOfEnd.minute - self.timeOfStart.minute

    def __str__(self):
        return self.table.name + " " + str(self.dayOfWeek) + " " + str(self.timeOfStart)



class StudyGroup(models.Model):

    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    lastName = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    middleName = models.CharField(max_length=255)

    def __str__(self):
        return "{0} {1} {2}".format(self.lastName, self.firstName, self.middleName)


class TimeTable(models.Model):


    name = models.CharField(max_length=255, blank=False, default='main')
    description = models.CharField(max_length=1024)
    owner = models.ForeignKey('core.User')

    #class Meta

    def __str__(self):
        return self.owner.username + " " + self.name

    def getCellsInDay(self):
        return self.cell_set.order_by('dayOfWeek')

