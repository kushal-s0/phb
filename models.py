from django.db import models
from Login_page.models import RegisterStudent

# Create your models here.

class CodeFile(models.Model):
    group_code = models.ForeignKey(RegisterStudent, on_delete=models.CASCADE, related_name="code_files")
    file = models.FileField(upload_to="uploads/code/")
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.group_code.groupCode} - Code File"

class DatabaseFile(models.Model):
    group_code = models.ForeignKey(RegisterStudent, on_delete=models.CASCADE, related_name="database_files")
    file = models.FileField(upload_to="uploads/database/")
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.group_code.groupCode} - Database File"

class DocumentFile(models.Model):
    group_code = models.ForeignKey(RegisterStudent, on_delete=models.CASCADE, related_name="document_files")
    file = models.FileField(upload_to="uploads/document/")
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.group_code.groupCode} - Document File"

class AdditionalFile(models.Model):
    group_code = models.ForeignKey(RegisterStudent, on_delete=models.CASCADE, related_name="additional_files")
    file = models.FileField(upload_to="uploads/additional/")
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.group_code.groupCode} - Additional File"
