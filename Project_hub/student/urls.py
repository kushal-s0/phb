from django.contrib import admin
from django.urls import path,include
from student import views

urlpatterns = [
    path('',views.homePage,name='Homepage')
]