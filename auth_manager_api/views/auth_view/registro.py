from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from auth_manager_api.serializers import UserSerializer


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
