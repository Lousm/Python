from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    pswd=models.CharField(max_length=200)
    eml=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=11,null=True)
    age=models.CharField(max_length=3,null=True)
    jianjie=models.TextField(null=True)
    sex=models.CharField(max_length=2,null=True)

