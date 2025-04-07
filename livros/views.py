from django.shortcuts import render
from .models import Livro
# Create your views here.

def read(request):
    try:
        livro = Livro.objects.all()
    except Exception as e:
        return render({f'erro': "{e}"})
    
    return render(request, "livros.html",  {'livros': livro})