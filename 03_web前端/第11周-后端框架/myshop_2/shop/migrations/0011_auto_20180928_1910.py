# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-28 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20180926_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_cart',
            name='price',
        ),
        migrations.RemoveField(
            model_name='shopping_cart',
            name='status',
        ),
        migrations.AddField(
            model_name='shopping_cart',
            name='add_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
