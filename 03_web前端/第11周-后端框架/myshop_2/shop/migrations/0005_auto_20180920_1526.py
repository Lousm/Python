# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-20 07:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_manage', '0002_auto_20180919_2115'),
        ('shop', '0004_auto_20180920_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='classify',
            name='add_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='classify',
            name='add_user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop_manage.Manage'),
        ),
    ]
