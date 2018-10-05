# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-19 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_manage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manage',
            name='add_time',
            field=models.CharField(default='00/00/00/ 00:00:00', max_length=50),
        ),
        migrations.AddField(
            model_name='manage',
            name='disable',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='manage',
            name='realname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
