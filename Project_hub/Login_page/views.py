from django.shortcuts import render,redirect
from Login_page.models import RegisterStudent
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.


def addProjectName(request):
    
    print(request.method)
    if  request.method == 'GET':
        projectName = request.POST.get('projectName')
        print(groupCode)
        register = RegisterStudent.objects.filter(groupCode = groupCode).values()
        print(register)
        
    return render(request,'addProjectName.html')

def studentLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        checkUsername = RegisterStudent.objects.filter(username = username).exists()
        if checkUsername:
            checkPassword = RegisterStudent.objects.filter(username = username,password = password).exists()
            if checkPassword:
                
                return redirect('/studentPage/')
            else:
                messages.warning(request, "incorrect password")
        else:
            messages.warning(request, "Usernam does not exist")
        # return render(request,'tp.html',{'members' :checkuser})

    return render(request,'studentLogin.html')

def registerStudent(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        year = request.POST.get('year')
        
        branch = request.POST.get('branch')
        groupNumber = request.POST.get('groupNumber')
        global groupCode
        groupCode = year+'_'+branch+'_'+groupNumber

        checkuser = RegisterStudent.objects.filter(username = username).count()
        
        if checkuser == 0:
            
            if len(password) < 8:
                messages.warning(request, "Password should have more than 8 characters")

            elif password == confirmPassword :

                register = RegisterStudent(name=name ,username=username ,email=email ,password=password,year = year,branch = branch,groupNumber = groupNumber,groupCode = groupCode)
                register.save()
                projName = RegisterStudent.objects.filter(groupCode = groupCode).values_list()
                
                projectName = projName[0][8]
                if(projectName == 'blank'):
                    return redirect('/addProjectName')
                messages.success(request, "Registration succesfull")
            else:
                messages.warning(request, "Password does not match")
        else:
            messages.warning(request, "Username already taken")
            
    
    return render(request,'registerStudent.html')

def guideLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username = username,groups__name = 'Guide'):
            print("entered")
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                #guide page
                return redirect('/guide/')
            else:
                messages.warning(request, "incorrect password")
                print("fail")
        else:
            messages.warning(request, "Username not present for guide")
            # if User.objects.filter(username = username,password = password).count() != 0:

            #     return render(request,'tp.html')
            # else:
            #     print("fail")

    #return render(request,'tp.html',{'users':user})
    return render(request,'guideLogin.html')


def evaluatorLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username = username,groups__name = 'Evaluator'):
            print("entered")
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                #evaluator page
                return redirect('/evaluator/')
            else:
                messages.warning(request, "incorrect password")
                print("fail")
        else:
            messages.warning(request, "Username not present for evaluator")   
    return render(request,'evaluatorLogin.html')

