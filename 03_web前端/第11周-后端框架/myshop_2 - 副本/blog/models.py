from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    xuehao=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
    jianjie=models.TextField()