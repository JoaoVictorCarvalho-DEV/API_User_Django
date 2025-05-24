from collections import defaultdict

from django.db.models import Q, Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from auth_manager_api.models import Tarefas
from auth_manager_api.serializers import TarefaSerializer
from auth_manager_api.serializers import TarefaSerializer
from drf_spectacular.utils import extend_schema

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
        summary="Listar todas as tarefas",
        description="""
        Retorna uma lista de todas as tarefas.
        Pode ser filtrada por `user_id` para listar tarefas de um responsável específico.
        """,
        parameters=[
            OpenApiParameter(
                name='user_id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description='ID do responsável para filtrar tarefas',
                required=False,
                examples=[
                    OpenApiExample(
                        'Exemplo',
                        value=1
                    )
                ]
            ),
        ],
        responses={
            200: TarefaSerializer(many=True),
            401: OpenApiResponse(description="Não autenticado"),
        },
        examples=[
            OpenApiExample(
                'Exemplo de resposta',
                value=[
                    {
                        "id": 1,
                        "nome": "Implementar autenticação",
                        "status": "Em andamento",
                        "responsavel_id": 1
                    }
                ],
                response_only=True,
            ),
        ],
    ),
    retrieve=extend_schema(
        summary="Detalhes de uma tarefa",
        description="Retorna os detalhes completos de uma tarefa específica.",
        responses={
            200: TarefaSerializer,
            404: OpenApiResponse(description="Tarefa não encontrada"),
        },
    ),
    create=extend_schema(
        summary="Criar nova tarefa",
        description="Cria uma nova tarefa no sistema.",
        request=TarefaSerializer,
        responses={
            201: TarefaSerializer,
            400: OpenApiResponse(description="Dados inválidos"),
        },
    ),
    update=extend_schema(
        summary="Atualizar tarefa",
        description="Atualiza todos os campos de uma tarefa existente.",
        request=TarefaSerializer,
        responses={
            200: TarefaSerializer,
            400: OpenApiResponse(description="Dados inválidos"),
            404: OpenApiResponse(description="Tarefa não encontrada"),
        },
    ),
    partial_update=extend_schema(
        summary="Atualização parcial de tarefa",
        description="Atualiza campos específicos de uma tarefa existente.",
        request=TarefaSerializer,
        responses={
            200: TarefaSerializer,
            400: OpenApiResponse(description="Dados inválidos"),
            404: OpenApiResponse(description="Tarefa não encontrada"),
        },
    ),
    destroy=extend_schema(
        summary="Excluir tarefa",
        description="Remove permanentemente uma tarefa do sistema.",
        responses={
            204: OpenApiResponse(description="Tarefa excluída com sucesso"),
            404: OpenApiResponse(description="Tarefa não encontrada"),
        },
    ),
)
class TarefaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciamento completo de tarefas.

    Permite operações CRUD padrão e endpoints customizados.
    As tarefas podem ser filtradas por responsável usando o parâmetro `user_id`.
    """
    queryset = Tarefas.objects.all()
    serializer_class = TarefaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')

        if user_id:
            queryset = queryset.filter(responsavel_id=user_id)

        return queryset

    @extend_schema(
        summary="Listar tarefas agrupadas por status",
        description="""
        Retorna todas as tarefas de um projeto específico,
        agrupadas por status em um formato de dicionário.
        """,
        parameters=[
            OpenApiParameter(
                name='id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                description='ID do projeto'
            )
        ],
        responses={
            200: OpenApiResponse(
                description="Dicionário de tarefas agrupadas por status",
                response=OpenApiTypes.OBJECT,
                examples=[
                    OpenApiExample(
                        'Exemplo de resposta',
                        value={
                            "Em andamento": [
                                {
                                    "id": 1,
                                    "nome": "Tarefa 1",
                                    "status": "Em andamento"
                                }
                            ],
                            "Concluído": [
                                {
                                    "id": 2,
                                    "nome": "Tarefa 2",
                                    "status": "Concluído"
                                }
                            ]
                        }
                    )
                ]
            ),
            404: OpenApiResponse(description="Projeto não encontrado"),
        },
        methods=["GET"]
    )
    @action(detail=True, methods=['get'])
    def tarefas_por_status(self, request, pk=None):
        projeto = self.get_object()
        tarefas = projeto.tarefas.all()

        grouped = defaultdict(list)
        for tarefa in tarefas:
            grouped[tarefa.status].append(TarefaSerializer(tarefa).data)

        return Response(grouped)

    @extend_schema(
        methods=['GET'],
        summary="Estatísticas gerais das tarefas",
        description="Retorna contagens de tarefas por status e total geral.",
        responses={200: OpenApiResponse(description="Estatísticas das tarefas")},
    )
    @action(detail=False, methods=['get'], url_path='statistics')
    def statistics(self, request):
        stats = Tarefas.objects.aggregate(
            cancelada=Count('id', filter=Q(status__iexact='Cancelada')),
            em_andamento=Count('id', filter=Q(status__iexact='Em andamento')),
            concluida=Count('id', filter=Q(status__iexact='Concluída')),
            total=Count('id')
        )
        return Response(stats)