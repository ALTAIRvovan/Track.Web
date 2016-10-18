from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    studyGroup = models.ForeignKey('study_calendar.StudyGroup')
