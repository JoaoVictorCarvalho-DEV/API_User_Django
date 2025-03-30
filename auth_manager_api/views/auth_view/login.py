from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
import rest_framework.generics

from auth_manager_api.serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
from auth_manager_api.models import CustomUser as User



# Create your views here.
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username= request.data['username'])#Verifica se existe
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

