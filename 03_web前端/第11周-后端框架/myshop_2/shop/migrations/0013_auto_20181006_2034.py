# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-06 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_user_receiving_address_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_form',
            name='add_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
