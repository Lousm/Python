# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-26 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_home_floor_paixu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home_floor',
            name='paixu',
        ),
        migrations.AddField(
            model_name='home_floor_commodity',
            name='paixu',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
