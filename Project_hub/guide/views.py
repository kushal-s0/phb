from django.shortcuts import render
from Login_page.models import RegisterStudent as reg
from django.contrib.auth.models import User
from guide.models import guide_groups
# Create your views here.

def start(request):

    return render(request,'guide.html')

def groups(request):
    return render(request,'groups\\groups.html')

def addGroup(request):
    currentUser = request.user
    
    
    data = reg.objects.values('groupCode','projectName').distinct()

    data_dict = {'data':data}

    if request.method == 'POST':
        
        groupCode = request.POST.getlist('code')
        
        
        for gc in groupCode:
            text = gc.split(',')
            print(text)
            
            register2 = guide_groups(groupCode = text[0],guide_name = currentUser,projectName = text[1])
            
            register2.save()

    return render(request,'addGroup\\addGroup.html',data_dict)