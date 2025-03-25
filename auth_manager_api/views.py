from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username= request.data['username'])#Verifica se existe
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        # Salva o usuário com os dados validados
        user = serializer.save()

        # Define a senha hasheada
        user.set_password(request.data['password'])
        user.save()

        # Cria um token para o usuário
        token = Token.objects.create(user=user)

        # Retorna o token e os dados do usuário
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)

    # Retorna os erros de validação do serializer
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def token(request):
    return Response("Passed for {}".format(request.user.email))