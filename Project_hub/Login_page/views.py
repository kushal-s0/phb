from django.shortcuts import render
from Login_page.models import RegisterStudent
from django.contrib import messages

# Create your views here.
def studentPage(request):
    return render(request,'loginPage.html')

def registerStudent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        print(password,confirmPassword)

        if password == confirmPassword :
            register = RegisterStudent(name=name ,username=username ,email=email ,password=password)
            register.save()
            messages.success(request, "Registration succesfull")
        else:
            messages.warning(request,"Error in registration:Password does not match")
    
    return render(request,'registerStudent.html')