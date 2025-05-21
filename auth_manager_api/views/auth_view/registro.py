from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from auth_manager_api.serializers import UserSerializer

from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample,
    OpenApiResponse,
    OpenApiRequest,
)


@extend_schema(
    # Configurações básicas
    summary="Registro de novo usuário",
    description="""
    Endpoint para criação de novas contas de usuário.
    Cria um novo usuário no sistema e retorna um token de autenticação imediatamente.
    A senha fornecida será hasheada antes de ser armazenada no banco de dados.
    """,
    methods=["POST"],
    tags=["Autenticação"],

    # Documentação da requisição
    request=UserSerializer,
    examples=[
        OpenApiExample(
            "Exemplo de requisição",
            value={
                "username": "novo_usuario",
                "password": "senhaSegura123",
                "email": "usuario@example.com",
                # Inclua aqui outros campos obrigatórios do seu UserSerializer
            },
            request_only=True
        ),
    ],

    # Documentação das respostas
    responses={
        201: OpenApiResponse(
            description="Usuário criado com sucesso",
            response={
                "type": "object",
                "properties": {
                    "token": {
                        "type": "string",
                        "example": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
                        "description": "Token de autenticação do novo usuário"
                    },
                    "user": {
                        "$ref": "#/components/schemas/User",
                        "description": "Dados do usuário recém-criado"
                    }
                }
            },
            examples=[
                OpenApiExample(
                    "Exemplo de resposta de sucesso",
                    value={
                        "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
                        "user": {
                            "id": 42,
                            "username": "novo_usuario",
                            "email": "usuario@example.com"
                        }
                    }
                )
            ]
        ),
        400: OpenApiResponse(
            description="Dados inválidos",
            response={
                "type": "object",
                "properties": {
                    "username": {
                        "type": "array",
                        "items": {"type": "string"},
                        "example": ["Este campo é obrigatório."]
                    },
                    "password": {
                        "type": "array",
                        "items": {"type": "string"},
                        "example": ["Este campo é obrigatório."]
                    },
                    # Adicione outros campos que podem retornar erros
                },
                "example": {
                    "username": ["Este campo é obrigatório."],
                    "password": ["Este campo deve conter pelo menos 8 caracteres."]
                }
            }
        ),
    }
)
@api_view(['POST'])
def signup(request):
    """
        Cria um novo usuário no sistema e retorna um token de acesso.

        Processo:
        1. Valida os dados de entrada usando o UserSerializer
        2. Cria o usuário com a senha hasheada
        3. Gera um token de autenticação
        4. Retorna o token e os dados do usuário

        Args:
            request (HttpRequest): Deve conter:
                - username (str): Nome de usuário único
                - password (str): Senha para autenticação
                - email (str): Endereço de e-mail (opcional dependendo do serializer)
                - [outros campos definidos no UserSerializer]

        Returns:
            Response: Em caso de sucesso (201), retorna:
                - token (str): Token de autenticação
                - user (dict): Dados do usuário criado
            Em caso de erro (400), retorna:
                - errors (dict): Dicionário com erros de validação
        """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        # Salva o usuário com os dados validados
        user = serializer.save()

        # Define a senha hasheada
        user.set_password(request.data['password'])
        user.save()

        # Cria um token para o usuário
        token = Token.objects.create(user=user)

        # Retorna o token e os dados do usuário
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)

    # Retorna os erros de validação do serializer
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
