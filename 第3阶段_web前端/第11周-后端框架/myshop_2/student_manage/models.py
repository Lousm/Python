from django.db import models

class Student(models.Model):
     name=models.CharField(max_length=100)
     num=models.IntegerField()
     sex=models.CharField(max_length=50)
     age=models.CharField(max_length=50)
     zhuanye=models.CharField(max_length=50)
     clas=models.CharField(max_length=50)

class Manage(models.Model):
    name = models.CharField(max_length=20)
    pswd = models.CharField(max_length=50)
