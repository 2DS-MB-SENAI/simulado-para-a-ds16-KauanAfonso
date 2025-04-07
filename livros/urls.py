from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('livros/templates/livros.html', views.Listar_Livros , name="Listar_Livros" ),
    path('api/livros/', views.Listar_Livros_API),

]
