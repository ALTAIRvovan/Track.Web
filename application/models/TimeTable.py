from django.db import models

from models import StudyGroup

class TimeTable(models.Model):

    owner_group = models.ForeignKey(StudyGroup)
