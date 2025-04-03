from rest_framework import viewsets
from rest_framework.response import Response

from auth_manager_api.models import Orgaos
from auth_manager_api.serializers import OrgaoSerializer


class OrgaoViewSet(viewsets.ModelViewSet):
    queryset = Orgaos.objects.all()
    serializer_class = OrgaoSerializer