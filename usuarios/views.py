from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Usuario     
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken




@api_view(['POST'])
def criar_usuario(request):

    username = request.data.get('username')
    password = request.data.get('password')
    telefone = request.data.get('telefone')

    if not username or not password or not telefone:
        return Response({"Erro":"Dados enviados incorretamente"}, status=status.HTTP_400_BAD_REQUEST)
    
    if Usuario.objects.filter(username=username).exists():
        return Response({'ERRO': "Usuario ja cadastrado"}, status=status.HTTP_400_BAD_REQUEST)
    
    user = Usuario.objects.create_user(
        username=username,
        password=password,
        telefone=telefone,
    )

    return Response({"usuário criado com sucesso": username}, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def logar(request):

    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')    


        usuario = authenticate(username=username, password=password)
        if usuario:
            refresh = RefreshToken.for_user(usuario)
            return Response({"Token": str(refresh.access_token), "Refresh":str(refresh)}, status=status.HTTP_200_OK)
        else:
            return Response({"Erro: Usuário ou senha inválidos"}, status=status.HTTP_401_UNAUTHORIZED)


