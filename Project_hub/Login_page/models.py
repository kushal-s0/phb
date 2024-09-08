from django.db import models

# Create your models here.

class RegisterStudent(models.Model):
    name = models.CharField(max_length=50)
    username=models.CharField(max_length=50).primary_key
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name