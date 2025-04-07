from django.shortcuts import render
from .models import Livro
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import LivroSerializer
# Create your views here.

def Listar_Livros(request):
    try:
        livro = Livro.objects.all()
    except Exception as e:
        return render({f'erro': "{e}"})
    
    return render(request, "livros.html",  {'livros': livro})


@api_view(['GET','POST'])
def Listar_Livros_API(request):
    if request.method == 'GET':
        todos_livros = Livro.objects.all()
        serializer = LivroSerializer(todos_livros, many=True)
        return Response({"livros":serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        try:
            serializer = LivroSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'Livro criado:':serializer.data }, status=status.HTTP_201_CREATED)
            return Response({'Erro:' "Erro de requisisão"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Erro: ': e}, status=status.HTTP_409_CONFLICT)