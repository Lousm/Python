# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-26 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20180926_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_floor',
            name='paixu',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
