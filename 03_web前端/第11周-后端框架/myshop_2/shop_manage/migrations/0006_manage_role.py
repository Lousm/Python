# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-09-25 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_manage', '0005_role_role_power'),
    ]

    operations = [
        migrations.AddField(
            model_name='manage',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop_manage.Role'),
            preserve_default=False,
        ),
    ]
