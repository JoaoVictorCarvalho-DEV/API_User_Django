from django.db.models import Q, Count
from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from auth_manager_api.models import Projetos, Mensagens, CustomUser
from auth_manager_api.models import Tarefas
from auth_manager_api.serializers import ProjetoSerializer, MensagemSerializer
from auth_manager_api.serializers import TarefaSerializer

from rest_framework.decorators import action, api_view, permission_classes

from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
    OpenApiExample,
    OpenApiResponse,
    OpenApiTypes,
)


@extend_schema_view(
    list=extend_schema(
        summary="Listar projetos",
        description="""
        Retorna uma lista de projetos. Se um `user_id` for fornecido como parâmetro,
        filtra os projetos onde o usuário é desenvolvedor, analista ou membro.
        """,
        parameters=[
            OpenApiParameter(
                name='user_id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description='ID do usuário para filtrar projetos associados',
                required=False,
            ),
        ],
        responses={
            200: ProjetoSerializer(many=True),
            401: OpenApiResponse(description="Não autenticado"),
        },
        examples=[
            OpenApiExample(
                'Exemplo de requisição',
                value={"user_id": 1},
                request_only=True,
            ),
            OpenApiExample(
                'Exemplo de resposta',
                value=[
                    {
                        "id": 1,
                        "nome": "Projeto Alpha",
                        "analista_id": 1,
                        "desenvolvedor_id": 2,
                    }
                ],
                response_only=True,
            ),
        ],
    ),
    retrieve=extend_schema(
        summary="Detalhes de um projeto",
        description="Retorna os detalhes de um projeto específico.",
        responses={
            200: ProjetoSerializer,
            404: OpenApiResponse(description="Projeto não encontrado"),
        },
    ),
    create=extend_schema(
        summary="Criar projeto",
        description="Cria um novo projeto (apenas para superusuários ou analistas).",
        responses={
            201: ProjetoSerializer,
            403: OpenApiResponse(description="Permissão negada"),
        },
    ),
    update=extend_schema(
        summary="Atualizar projeto",
        description="Atualiza um projeto existente (apenas para superusuários ou analistas).",
    ),
    destroy=extend_schema(
        summary="Excluir projeto",
        description="Exclui um projeto (apenas para superusuários ou analistas).",
    ),
)
class ProjetoViewSet(viewsets.ModelViewSet):
    """
        ViewSet para gerenciar Projetos.

        Permite operações CRUD e ações customizadas (tarefas, mensagens, membros).
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

    @extend_schema(
        methods=['GET'],
        summary="Listar tarefas do projeto",
        description="Retorna todas as tarefas de um projeto, ordenadas por data final.",
        responses={
            200: TarefaSerializer(many=True),
            404: OpenApiResponse(description="Projeto não encontrado"),
        },
    )
    @action(detail=True, methods=['get'])
    def tarefas(self, request, pk=None):
        projeto = self.get_object()
        tarefas_ordenadas = projeto.tarefas.order_by('data_final')
        print([t.data_final for t in tarefas_ordenadas])
        serializer = TarefaSerializer(tarefas_ordenadas, many=True)
        return Response(serializer.data)
    @extend_schema(
        methods=['GET', 'POST'],
        summary="Gerenciar mensagens do projeto",
        description="""
        - **GET**: Lista todas as mensagens do projeto.
        - **POST**: Cria uma nova mensagem (apenas para membros do projeto).
        """,
        request=MensagemSerializer,
        responses={
            200: MensagemSerializer(many=True),  # GET
            201: MensagemSerializer,             # POST
            403: OpenApiResponse(description="Usuário não é membro do projeto"),
        },
        examples=[
            OpenApiExample(
                'Exemplo de POST',
                value={
                    "user_id": 1,
                    "conteudo": "Olá, equipe!",
                },
                request_only=True,
            ),
        ],
    )
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

    @extend_schema(
        methods=['POST'],
        summary="Adicionar membro ao projeto",
        description="""
            Adiciona um usuário como membro do projeto.
            Requer permissão de superusuário ou analista do projeto.
            """,
        request=OpenApiTypes.OBJECT,
        responses={
            200: OpenApiResponse(description="Usuário adicionado com sucesso"),
            403: OpenApiResponse(description="Permissão negada"),
            404: OpenApiResponse(description="Usuário não encontrado"),
        },
        examples=[
            OpenApiExample(
                'Exemplo de requisição',
                value={"user_id": 3},
                request_only=True,
            ),
        ],
    )
    @action(detail=True, methods=['post'])
    def adicionar_membro(self, request, pk=None):
        projeto = self.get_object()
        user_id = request.data.get('user_id')
        solicitante = request.user

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

    @extend_schema(
        methods=['POST'],
        summary="Remover membros do projeto",
        description="""
            Remove múltiplos usuários da lista de membros do projeto.
            Requer permissão de superusuário ou analista do projeto.
            """,
        request=OpenApiTypes.OBJECT,
        responses={
            200: OpenApiResponse(description="Membros removidos com sucesso"),
            403: OpenApiResponse(description="Permissão negada"),
        },
        examples=[
            OpenApiExample(
                'Exemplo de requisição',
                value={"user_ids": [3, 4]},
                request_only=True,
            ),
        ],
    )
    @action(detail=True, methods=['post'])
    def remover_membros(self, request, pk=None):
        projeto = self.get_object()
        user_ids = request.data.get('user_ids', [])
        users = CustomUser.objects.filter(id__in=user_ids)
        projeto.membros.remove(*users)
        projeto.save()
        return Response({'status': 'membros removidos'})

    @extend_schema(
        methods=['GET'],
        summary="Estatísticas gerais dos projetos",
        description="Retorna contagens de projetos por status e total geral.",
        responses={200: OpenApiResponse(description="Estatísticas dos projetos")},
    )
    @action(detail=False, methods=['get'], url_path='statistics')
    def statistics(self, request):
        stats = Projetos.objects.aggregate(
            em_andamento=Count('id', filter=Q(status__iexact='Em andamento')),
            concluido=Count('id', filter=Q(status__iexact='Concluída')),
            cancelada=Count('id', filter=Q(status__iexact='Cancelada')),
            total=Count('id')
        )
        return Response(stats)
