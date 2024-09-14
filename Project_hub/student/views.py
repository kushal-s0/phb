from django.shortcuts import render,redirect

# Create your views here.
def homePage(request):
    print("working")
    return render(request,'student\\home.html')

def search(request):
    return render(request,'student\\search.html')

def upload(request):
    return render(request,'student\\upload.html')

def resources(request):
    return render(request,'student\\resources.html')