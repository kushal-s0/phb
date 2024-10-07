from django import forms
from .models import CodeFile, DatabaseFile,DocumentFile,AdditionalFile

class FileEditForm(forms.ModelForm):
    class Meta:
        model = CodeFile
        fields = ['name', 'content','file','file_type','group_code']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 20, 'cols': 100}),
        }



class CodeFileForm(forms.ModelForm):
    class Meta:
        model = CodeFile
        fields = ['group_code', 'file', 'file_type', 'name', 'content'] 
