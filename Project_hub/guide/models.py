from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class guide_groups(models.Model):
    groupCode = models.CharField(max_length=60,primary_key=True)
    guide_name = models.ForeignKey(User, on_delete=models.CASCADE)
    projectName = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.guide_name.first_name
    
    class Meta:
        verbose_name_plural = "Guide_group"