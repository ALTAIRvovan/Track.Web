from django.conf import settings
from django.db import models


# Create your models here.


class Comment(models.Model):
    text = models.TextField(default="text")
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    cell = models.ForeignKey('study_calendar.Cell')

    def __str__(self):
        return str(self.cell) + " " + str(self.author)
