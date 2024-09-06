from django.shortcuts import render


# Create your views here.
def studentPage(request):
    return render(request,'loginPage.html')

def registerStudent(request):
    return render(request,'registerStudent.html')