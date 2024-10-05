from django.shortcuts import render,redirect
from django.contrib import messages
# from student.models import UploadedFile
from Login_page.models import RegisterStudent

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
    return render(request, 'student/uploads/code.html')

# Folder View Page
def document_view(request):
    return render(request, 'student/uploads/document.html')

# Additional View Page
def additional_view(request):
    return render(request, 'student/uploads/additional.html')

# Database View Page
def database_view(request):
    return render(request, 'student/uploads/database.html')

#View Details Page
def view_details(request):
    return render(request, 'student/uploads/view.html')