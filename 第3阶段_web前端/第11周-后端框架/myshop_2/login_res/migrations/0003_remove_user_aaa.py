# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-12 13:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_res', '0002_user_aaa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='aaa',
        ),
    ]
