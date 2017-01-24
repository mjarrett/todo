# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20170124_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
