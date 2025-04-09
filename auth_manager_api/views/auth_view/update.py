from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from auth_manager_api.serializers import UserSerializer
from auth_manager_api.models import CustomUser


@api_view(['PUT'])
def update(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({"error": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    # Se o campo 'password' foi enviado, trate ele separadamente
    password = request.data.get('password')

    # Serializa os outros dados (exceto a senha)
    serializer = UserSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        updated_user = serializer.save()

        # Se foi enviada uma nova senha, defina com hashing
        if password:
            updated_user.set_password(password)
            updated_user.save()

        return Response({
            "message": "Usuário atualizado com sucesso",
            "user": UserSerializer(updated_user).data  # Re-serializa para refletir atualizações
        })

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

