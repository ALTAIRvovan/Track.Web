# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('study_calendar', '0006_auto_20161017_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('timeOfStart', models.TimeField()),
                ('timeOfEnd', models.TimeField()),
                ('dateOfStart', models.DateField()),
                ('dateOfEnd', models.DateField()),
                ('dayOfWeek', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=255)),
                ('firstName', models.CharField(max_length=255)),
                ('middleName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_calendar.StudyGroup')),
            ],
        ),
        migrations.AddField(
            model_name='cell',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_calendar.TimeTable'),
        ),
        migrations.AddField(
            model_name='cell',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study_calendar.Teacher'),
        ),
    ]