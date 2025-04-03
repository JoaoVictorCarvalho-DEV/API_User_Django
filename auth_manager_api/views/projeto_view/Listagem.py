from rest_framework import viewsets
from rest_framework.response import Response

from auth_manager_api.models import Projetos
from auth_manager_api.models import Tarefas
from auth_manager_api.serializers import ProjetoSerializer
from auth_manager_api.serializers import TarefaSerializer

from rest_framework.decorators import action

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projetos.objects.all()
    serializer_class = ProjetoSerializer

    @action(detail=True, methods=['get'])
    def tarefas(self,request,pk=None):
        projeto = self.get_object()
        serializer = TarefaSerializer(projeto.tarefas.all(), many=True)
        return Response(serializer.data)
