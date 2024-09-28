from django.db import models

# Create your models here.

class RegisterStudent(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,primary_key=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    groupCode = models.CharField(max_length=10)
    year = models.CharField(max_length=5,default='00')
    branch = models.CharField(max_length=10,default='00')
    groupNumber = models.CharField(max_length=5,default='00')
    projectName = models.CharField(max_length=100,default='blank')
    projYear = models.CharField(max_length=15,default='00')

    def __str__(self):
        return self.name
    

