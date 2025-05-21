from rest_framework import viewsets
from rest_framework.response import Response

from auth_manager_api.models import CustomUser, Atores
from auth_manager_api.serializers import UserSerializer, AtoresSerializer

from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
    OpenApiExample,
    OpenApiResponse,
    OpenApiTypes,
)
@extend_schema(
    tags=["Ator"],
    description="Operações relacionadas aos usuários do sistema que atuam como Atores.",
    parameters=[
        OpenApiParameter(name='search', type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, required=False, description='Filtrar atores por nome ou email')
    ],
    responses={
        200: OpenApiResponse(response=UserSerializer(many=True), description="Lista de usuários (atores)"),
        201: OpenApiResponse(response=UserSerializer, description="Usuário criado com sucesso"),
        400: OpenApiResponse(description="Dados inválidos"),
    },
    examples=[
        OpenApiExample(
            name="Exemplo de retorno de lista de atores",
            value=[
                {"id": 1, "username": "joao", "email": "joao@example.com"},
                {"id": 2, "username": "maria", "email": "maria@example.com"}
            ],
            response_only=True
        )
    ]
)
class AtorViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

@extend_schema(
    tags=["Papel"],
    description="CRUD dos papéis que os atores podem desempenhar nos projetos.",
    parameters=[
        OpenApiParameter(name='ator_id', type=OpenApiTypes.INT, location=OpenApiParameter.QUERY, required=False, description='Filtrar papéis por ID do ator')
    ],
    responses={
        200: OpenApiResponse(response=AtoresSerializer(many=True), description="Lista de papéis"),
        201: OpenApiResponse(response=AtoresSerializer, description="Papel criado com sucesso"),
        400: OpenApiResponse(description="Erro ao processar solicitação")
    },
    examples=[
        OpenApiExample(
            name="Exemplo de criação de papel",
            value={
                "ator": 1,
                "descricao": "Desenvolvedor Backend"
            },
            request_only=True
        )
    ]
)
class PapelViewSet(viewsets.ModelViewSet):
    queryset = Atores.objects.all()
    serializer_class = AtoresSerializer