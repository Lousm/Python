# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-13 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_res', '0005_auto_20180913_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
