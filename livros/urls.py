from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('templates/', views.Listar_Livros , name="Listar Livros" ),
    path('api/livros', views.Listar_Livros_API)
]
