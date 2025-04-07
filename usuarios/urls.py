from django.urls import path
from .views import *

urlpatterns = [
    path("registro/", criar_usuario),
    path("login/", logar)
]
