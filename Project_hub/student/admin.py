from django import forms
from django.contrib import admin
from .models import CodeFile, DatabaseFile, DocumentFile, AdditionalFile
from Login_page.models import RegisterStudent

class CodeFileAdminForm(forms.ModelForm):
    class Meta:
        model = CodeFile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CodeFileAdminForm, self).__init__(*args, **kwargs)
        # Customize the queryset for the ForeignKey to display group codes
        self.fields['group_code'].queryset = RegisterStudent.objects.all()
        self.fields['group_code'].label_from_instance = lambda obj: obj.groupCode

class CodeFileAdmin(admin.ModelAdmin):
    form = CodeFileAdminForm
    list_filter = ('group_code__groupCode','upload_date')
    list_display = ('get_group_code', 'file', 'upload_date')
    
    def get_group_code(self, obj):
        return obj.group_code.groupCode

    get_group_code.short_description = 'Group Code'
    
class DatabaseFileAdmin(admin.ModelAdmin):
    form = CodeFileAdminForm  # You can reuse the same form for each model if they share the same behavior
    list_filter = ('group_code__groupCode','upload_date')
    list_display = ('get_group_code', 'file', 'upload_date')
    
    def get_group_code(self, obj):
        return obj.group_code.groupCode

    get_group_code.short_description = 'Group Code'

class DocumentFileAdmin(admin.ModelAdmin):
    form = CodeFileAdminForm
    list_filter = ('group_code__groupCode','upload_date')
    list_display = ('get_group_code', 'file', 'upload_date')
    
    def get_group_code(self, obj):
        return obj.group_code.groupCode

    get_group_code.short_description = 'Group Code'

class AdditionalFileAdmin(admin.ModelAdmin):
    form = CodeFileAdminForm
    list_filter = ('group_code__groupCode','upload_date')
    list_display = ('get_group_code', 'file', 'upload_date')
    
    def get_group_code(self, obj):
        return obj.group_code.groupCode

    get_group_code.short_description = 'Group Code'

admin.site.register(CodeFile, CodeFileAdmin)
admin.site.register(DatabaseFile, DatabaseFileAdmin)
admin.site.register(DocumentFile, DocumentFileAdmin)
admin.site.register(AdditionalFile, AdditionalFileAdmin)