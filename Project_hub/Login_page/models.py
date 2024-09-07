from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(50)
    username=models.CharField(50)
    email=models.EmailField(max_length=50)
    password=models.CharField(50)
