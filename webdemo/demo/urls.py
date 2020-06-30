
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('about/', views.about),
    path('employees/', views.list_employees),
]
