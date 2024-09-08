from django.shortcuts import render
from Login_page.models import RegisterStudent
from django.contrib import messages

# Create your views here.
def studentPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        checkuser = RegisterStudent.objects.filter(username = username,password = password).values
        
        return render(request,'tp.html',{'members' :checkuser})

    return render(request,'loginPage.html')

def registerStudent(request):
   
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        checkuser = RegisterStudent.objects.filter(username = username)
        if(checkuser is FileNotFoundError):
            if len(password) < 8:
                messages.warning(request, "Password should have more than 8 characters")

            elif password == confirmPassword :

                register = RegisterStudent(name=name ,username=username ,email=email ,password=password)
                register.save()
                messages.success(request, "Registration succesfull")
            else:
                messages.warning(request, "Password does not match")
        else:
            messages.warning(request, "Username already taken")
            
    
    return render(request,'registerStudent.html')