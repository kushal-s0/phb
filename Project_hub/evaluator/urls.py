from django.urls import path
from evaluator import views

urlpatterns = [
    path('',views.start,name='start'),
]