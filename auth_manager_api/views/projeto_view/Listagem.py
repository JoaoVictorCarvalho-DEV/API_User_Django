from django.db.models import Q
from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from auth_manager_api.models import Projetos, Mensagens
from auth_manager_api.models import Tarefas
from auth_manager_api.serializers import ProjetoSerializer, MensagemSerializer
from auth_manager_api.serializers import TarefaSerializer

from rest_framework.decorators import action, api_view, permission_classes


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


class MensagemListCreateView(ListCreateAPIView):
    serializer_class = MensagemSerializer

    def get_queryset(self):
        projeto_id = self.kwargs['projeto_id']
        return Mensagens.objects.filter(projeto_id=projeto_id)

    def create(self, request, *args, **kwargs):


        user_id = request.data.get('user_id')
        msg = request.data.get('conteudo')

        projeto_id = self.kwargs['projeto_id']
        projeto = get_object_or_404(Projetos, id=projeto_id)

        # Verifica se o user_id está entre os envolvidos no projeto
        if user_id not in [projeto.analista_id_id, projeto.desenvolvedor_id_id]:

            return Response(
                {"detail": "Usuário não faz parte do projeto."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Cria a mensagem
        mensagem = Mensagens.objects.create(
            projeto_id=projeto,
            user_id_id=user_id,
            conteudo=msg
        )

        serializer = MensagemSerializer(mensagem)
        return Response(serializer.data, status=status.HTTP_201_CREATED)