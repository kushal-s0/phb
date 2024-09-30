from django.shortcuts import render
from Login_page.models import RegisterStudent as reg

# Create your views here.
def start(request):

    return render(request,'guide.html')

def groups(request):
    return render(request,'groups\\groups.html')

def addGroup(request):
    data = reg.objects.values('groupCode','projectName').distinct()

    data_dict = {'data':data}

    if request.method == 'POST':
        
        groupCode = request.POST.getlist('code')
        print(groupCode)

    return render(request,'addGroup\\addGroup.html',data_dict)