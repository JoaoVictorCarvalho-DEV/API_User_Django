from rest_framework import viewsets
from rest_framework.response import Response

from auth_manager_api.models import Tarefas
from auth_manager_api.serializers import TarefaSerializer
from auth_manager_api.serializers import TarefaSerializer

#Uma view para o CRUD
class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefas.objects.all()
    serializer_class = TarefaSerializer
