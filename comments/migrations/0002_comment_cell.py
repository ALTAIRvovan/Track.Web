# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study_calendar', '0008_timetable_name'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='cell',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='study_calendar.Cell'),
            preserve_default=False,
        ),
    ]
