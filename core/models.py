from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    timetables = models.ManyToManyField('study_calendar.TimeTable')
