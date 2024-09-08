from django.contrib import admin
from django.urls import path
from Login_page import views

urlpatterns = [
    path("",views.studentPage,name="Sudent page"),
    path("loginPage/",views.studentPage,name="Sudent page"),
    path('registerStudent/',views.registerStudent,name="register Student"),
    
]