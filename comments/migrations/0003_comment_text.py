# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_cell'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default='text'),
        ),
    ]