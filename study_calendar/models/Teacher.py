from django.db import models
from django.contrib import admin


class Teacher(models.Model):
    lastName = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    middleName = models.CharField(max_length=255)

admin.site.register(Teacher)