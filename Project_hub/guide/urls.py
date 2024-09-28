from django.urls import path
from guide import views

urlpatterns = [
    path('',views.start,name='start'),
    path('groups/',views.groups,name='groups'),
    path('addGroup/',views.addGroup,name='addGroup'),
]
