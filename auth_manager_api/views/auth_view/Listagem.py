from rest_framework import viewsets
from rest_framework.response import Response

from auth_manager_api.models import CustomUser, Atores
from auth_manager_api.serializers import UserSerializer, AtoresSerializer


class AtorViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class PapelViewSet(viewsets.ModelViewSet):
    queryset = Atores.objects.all()
    serializer_class = AtoresSerializer