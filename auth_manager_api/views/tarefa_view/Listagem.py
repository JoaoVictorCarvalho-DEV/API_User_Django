from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response

from auth_manager_api.models import Tarefas
from auth_manager_api.serializers import TarefaSerializer
from auth_manager_api.serializers import TarefaSerializer


# Uma view para o CRUD
class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefas.objects.all()
    serializer_class = TarefaSerializer

    def get_queryset(self):
        queryset = Tarefas.objects.all()
        user_id = self.request.GET.get('user_id', None)

        if user_id:
            queryset = queryset.filter(responsavel_id=user_id)

        return queryset
