from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
# from student.models import UploadedFile
from Login_page.models import RegisterStudent
from .models import CodeFile,DatabaseFile,DocumentFile,AdditionalFile
from .forms import CodeFileForm,FileEditForm
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
    databasefile =DatabaseFile.objects.all()
    codefile =CodeFile.objects.all()
    documentfile =DocumentFile.objects.all()
    additionalfile = AdditionalFile.objects.all()
    return render(request, 'view\\view.html',{'databaseFile': databasefile, 'documentFile': documentfile,'codeFile': codefile,'additionalFile': additionalfile})


# def view_folder(request, folder_id):
#     folder = get_object_or_404(DocumentFile, id=folder_id)
#     files = folder.files.all()  # Get all files in this folder
#     return render(request, 'view_folder.html', {'folder': folder, 'files': files})


def edit_code_file(request, code_file_id):
    code_file = get_object_or_404(CodeFile, id=code_file_id)

    if request.method == 'POST':
        form = CodeFileForm(request.POST, request.FILES, instance=code_file)
        if form.is_valid():
            form.save()
            return redirect('upload_code_file')
    else:
        form = CodeFileForm(instance=code_file)

    return render(request, 'view\\edit_file.html', {'form': form, 'code_file': code_file})


def display_file_content(request, codefile_id):
    codefile = get_object_or_404(CodeFile, id=codefile_id)
    return render(request, 'display_file.html', {
        'file_content': codefile.content,
        'file_name': codefile.name,
        'file_id': codefile.id,
    })

def upload_code_file(request):
    if request.method == 'POST':
        code_file_form = CodeFileForm(request.POST, request.FILES,prefix='code')
        if code_file_form.is_valid():
            code_file_form.save()
            return redirect('upload_code_file')
        else:
            print(code_file_form.errors)
    else:
        code_file_form = CodeFileForm(prefix='code')

    code_files = CodeFile.objects.all()  # Retrieve all code files to display
    return render(request, 'uploads\\code.html', {'code_file_form': code_file_form, 'code_files': code_files})