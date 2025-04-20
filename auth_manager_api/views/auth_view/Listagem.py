from rest_framework import viewsets
from rest_framework.response import Response

from auth_manager_api.models import CustomUser
from auth_manager_api.serializers import UserSerializer

class AtorViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer