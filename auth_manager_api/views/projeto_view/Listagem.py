from django.db.models import Q
from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from auth_manager_api.models import Projetos, Mensagens, CustomUser
from auth_manager_api.models import Tarefas
from auth_manager_api.serializers import ProjetoSerializer, MensagemSerializer
from auth_manager_api.serializers import TarefaSerializer

from rest_framework.decorators import action, api_view, permission_classes


class ProjetoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar Projetos.

    Esta view permite listar e recuperar projetos. Caso um `user_id` seja passado
    na requisição como parâmetro GET, retorna apenas os projetos onde o usuário está
    associado, seja como desenvolvedor, analista ou membro.

    Attributes:
        queryset (QuerySet): Lista de todos os projetos disponíveis.
        serializer_class (Serializer): Serializador utilizado para representar os projetos.

    Methods:
        get_queryset(self):
            Obtém a lista de projetos, filtrando por `user_id` caso fornecido.

        tarefas(self, request, pk=None):
            Retorna todas as tarefas associadas a um projeto específico.
    """

    permission_classes = [IsAuthenticated]
    queryset = Projetos.objects.all()
    serializer_class = ProjetoSerializer

    def get_queryset(self):
        queryset = Projetos.objects.all()
        user_id = self.request.GET.get('user_id', None)

        if user_id:
            queryset = queryset.filter(
                Q(desenvolvedor_id=user_id) |
                Q(analista_id=user_id) |
                Q(membros__id=user_id)
            ).distinct()

        return queryset

    @action(detail=True, methods=['get'])
    def tarefas(self, request, pk=None):
        projeto = self.get_object()
        tarefas_ordenadas = projeto.tarefas.order_by('data_final')
        print([t.data_final for t in tarefas_ordenadas])
        serializer = TarefaSerializer(tarefas_ordenadas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get', 'post'])
    def mensagens(self, request, pk=None):
        projeto = self.get_object()

        if request.method == 'GET':
            mensagens = Mensagens.objects.filter(projeto_id=projeto)
            serializer = MensagemSerializer(mensagens, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            user_id = request.data.get('user_id')
            conteudo = request.data.get('conteudo')

            # Verifica se user_id está relacionado ao projeto
            membros_ids = list(projeto.membros.values_list('id', flat=True))
            if user_id not in [projeto.analista_id_id, projeto.desenvolvedor_id_id] and int(user_id) not in membros_ids:
                return Response(
                    {"detail": "Usuário não faz parte do projeto."},
                    status=status.HTTP_403_FORBIDDEN
                )

            mensagem = Mensagens.objects.create(
                projeto_id=projeto,
                user_id_id=user_id,
                conteudo=conteudo
            )
            serializer = MensagemSerializer(mensagem)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def adicionar_membro(self, request, pk=None):
        print("Usuário autenticado:", request.user)
        print("É autenticado?", request.user.is_authenticated)
        projeto = self.get_object()
        user_id = request.data.get('user_id')
        solicitante = request.user
        print(solicitante)

        # Verifica se o solicitante é admin ou analista do projeto
        if not (solicitante.is_superuser or solicitante.id == projeto.analista_id_id):
            return Response(
                {"detail": "Você não tem permissão para adicionar membros a este projeto."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            usuario = CustomUser.objects.get(id=user_id)
            projeto.membros.add(usuario)
            return Response({"detail": "Usuário adicionado com sucesso ao projeto."})
        except CustomUser.DoesNotExist:
            return Response({"detail": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def remover_membros(self, request, pk=None):
        projeto = self.get_object()
        user_ids = request.data.get('user_ids', [])
        users = CustomUser.objects.filter(id__in=user_ids)
        projeto.membros.remove(*users)
        projeto.save()
        return Response({'status': 'membros removidos'})

