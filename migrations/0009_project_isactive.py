# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_task_date_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
    ]
