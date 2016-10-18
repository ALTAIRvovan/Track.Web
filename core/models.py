from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    studyGroup = models.ManyToManyField('study_calendar.StudyGroup')
