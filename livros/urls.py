from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('templates/', views.read , name="read" )
]
