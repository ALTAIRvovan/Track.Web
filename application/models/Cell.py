from django.db import models
from models import TimeTable


class Cell(models.Model):

    table = models.ForeignKey(TimeTable)
    