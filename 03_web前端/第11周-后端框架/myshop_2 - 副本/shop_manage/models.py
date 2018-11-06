from django.db import models


class Manage(models.Model):
    admin_name = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    realname = models.CharField(max_length=50, null=True)
    add_time = models.CharField(max_length=50, default='00/00/00/ 00:00:00')
    disable = models.CharField(max_length=2, default=0)
    role = models.ForeignKey('Role')


class Power(models.Model):
    name = models.CharField(max_length=30)
    parent_id = models.CharField(max_length=3, default='0')
    control = models.CharField(max_length=50, null=True)
    urlname = models.CharField(max_length=50, null=True)
    fun = models.CharField(max_length=50, null=True)

class Role(models.Model):
    name = models.CharField(max_length=30)
    add_time = models.DateTimeField(auto_now=True)

class role_power(models.Model):
    role=models.ForeignKey('Role')
    power=models.ForeignKey('Power')
