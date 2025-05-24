from rest_framework import viewsets
from rest_framework.response import Response

from django.db.models import Count, Q
from rest_framework.decorators import action
from rest_framework.response import Response

from auth_manager_api.models import Orgaos
from auth_manager_api.serializers import OrgaoSerializer

from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
    OpenApiExample,
    OpenApiResponse,
    OpenApiTypes,
)

@extend_schema(
    tags=["Órgãos"],
    description="CRUD dos órgãos públicos vinculados aos projetos.",
    parameters=[
        OpenApiParameter(
            name="search",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            required=False,
            description="Filtrar órgãos pelo nome ou sigla"
        )
    ],
    responses={
        200: OpenApiResponse(
            response=OrgaoSerializer(many=True),
            description="Lista de órgãos"
        ),
        201: OpenApiResponse(
            response=OrgaoSerializer,
            description="Órgão criado com sucesso"
        ),
        400: OpenApiResponse(
            description="Erro na requisição. Verifique os dados enviados."
        ),
    },
    examples=[
        OpenApiExample(
            name="Exemplo de resposta - Lista de Órgãos",
            value=[
                {"id": 1, "nome": "Secretaria de Educação", "sigla": "SEDUC"},
                {"id": 2, "nome": "Secretaria de Saúde", "sigla": "SES"}
            ],
            response_only=True
        ),
        OpenApiExample(
            name="Exemplo de criação de órgão",
            value={
                "nome": "Secretaria de Meio Ambiente",
                "sigla": "SEMA"
            },
            request_only=True
        ),
    ]
)
class OrgaoViewSet(viewsets.ModelViewSet):
    queryset = Orgaos.objects.all()
    serializer_class = OrgaoSerializer

    @extend_schema(
        methods=['GET'],
        summary="Estatísticas dos órgãos",
        description="Retorna a quantidade de projetos vinculados a cada órgão.",
        responses={
            200: OpenApiResponse(description="Lista com órgãos e quantidade de projetos vinculados"),
        }
    )
    @action(detail=False, methods=['get'], url_path='statistics')
    def statistics(self, request):
        from auth_manager_api.models import Orgaos  # ou ajuste o import conforme sua estrutura
        data = (
            Orgaos.objects
            .annotate(total_projetos=Count('projetos'))  # nome do related_name do FK de Projeto para Orgao
            .values('nome', 'total_projetos')
        )
        return Response(data)