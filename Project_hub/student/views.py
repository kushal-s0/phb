from django.shortcuts import render

# Create your views here.
def homePage(request):
    print("working")
    return render(request,'tp.html')