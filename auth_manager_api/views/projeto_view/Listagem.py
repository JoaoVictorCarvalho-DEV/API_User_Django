from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request

from auth_manager_api.models import Projetos
from auth_manager_api.models import Tarefas
from auth_manager_api.serializers import ProjetoSerializer
from auth_manager_api.serializers import TarefaSerializer

from rest_framework.decorators import action


class ProjetoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar Projetos.

    Esta view permite listar e recuperar projetos. Caso um `user_id` seja passado
    na requisição como parâmetro, retorna apenas os projetos onde o usuário é um
    desenvolvedor ou analista.

    Attributes:
        queryset (QuerySet): Lista de todos os projetos disponíveis.
        serializer_class (Serializer): Serializador utilizado para representar os projetos.

    Methods:
        get_queryset(self):
            Obtém a lista de projetos, filtrando por `user_id` caso fornecido.

        tarefas(self, request, pk=None):
            Retorna todas as tarefas associadas a um projeto específico.
    """

    queryset = Projetos.objects.all()
    serializer_class = ProjetoSerializer

    def get_queryset(self):
        queryset = Projetos.objects.all()
        user_id = self.request.GET.get('user_id', None)

        if user_id:
            queryset = queryset.filter(
                Q(desenvolvedor_id=user_id) | Q(analista_id=user_id)
            )  # Usamos Q para combinar filtros com OR

        return queryset

    @action(detail=True, methods=['get'])
    def tarefas(self, request, pk=None):
        projeto = self.get_object()
        serializer = TarefaSerializer(projeto.tarefas.all(), many=True)
        return Response(serializer.data)
