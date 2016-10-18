from django.db import models
from django.contrib import admin

class StudyGroup(models.Model):

    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name


admin.site.register(StudyGroup)