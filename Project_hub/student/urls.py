from django.contrib import admin
from django.urls import path,include
from student import views

urlpatterns = [
    path('',views.homePage,name='Homepage'),
    path('homepage/',views.homePage,name='Homepage'),
    path('search/',views.search,name = 'Search'),
    path('resources/',views.resources,name = 'Resources'),
    path('upload/',views.upload,name = 'Upload'),
    path('homepage/file/',views.group_file,name = 'File'),
    path('homepage/groups/',views.group_groups,name = 'Groups'),
]