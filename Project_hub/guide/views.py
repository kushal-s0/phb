from django.shortcuts import render

# Create your views here.
def start(request):

    return render(request,'guide.html')

def groups(request):
    return render(request,'groups\\groups.html')

def addGroup(request):
    return render(request,'addGroup\\addGroup.html')