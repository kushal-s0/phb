from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
# from student.models import UploadedFile
from Login_page.models import RegisterStudent
from .models import CodeFile,DatabaseFile,DocumentFile,AdditionalFile

# Create your views here.
def homePage(request):
    print("working")
    return render(request,'student\\home.html')

def search(request):
    return render(request,'student\\search.html')

def resources(request):
    return render(request,'student\\resources.html')

def group_file(request):
    return render(request,'group\\file.html')

def group_groups(request):
    return render(request,'group\\groups.html')

def code(request):
    return render(request, 'uploads\\code.html')

# Folder View Page
def document_view(request):
    return render(request, 'uploads\\document.html')

# Additional View Page
def additional_view(request):
    return render(request, 'uploads\\additional.html')

# Database View Page
def database_view(request):
    return render(request, 'uploads\\database.html')

#View Details Page
def view_details(request):
    # databaseFile =DatabaseFile.objects.all()
    # codeFile =CodeFile.objects.all()
    # documentFile =DocumentFile.objects.all()
    # additionalFile = AdditionalFile.objects.all()
    return render(request, 'view\\view.html')


# def view_folder(request, folder_id):
#     folder = get_object_or_404(DocumentFile, id=folder_id)
#     files = folder.files.all()  # Get all files in this folder
#     return render(request, 'view_folder.html', {'folder': folder, 'files': files})