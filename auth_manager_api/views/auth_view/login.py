from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
import rest_framework.generics

from auth_manager_api.serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
from auth_manager_api.models import CustomUser as User



from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiExample,
    OpenApiResponse,
    OpenApiTypes,
)

@extend_schema(
    # Configuração básica do endpoint
    summary="Autenticação de usuário",
    description="""
    Endpoint para autenticação de usuários.
    Verifica as credenciais e retorna um token de autenticação válido
    junto com os dados do usuário se as credenciais estiverem corretas.
    """,
    methods=["POST"],
    # Documentação dos parâmetros de requisição
    request={
        "type": "object",
        "properties": {
            "username": {"type": "string", "description": "Nome de usuário"},
            "password": {"type": "string", "description": "Senha do usuário"},
        },
        "required": ["username", "password"],
        "example": {
            "username": "admin",
            "password": "senha123"
        }
    },
    # Documentação das respostas possíveis
    responses={
        200: OpenApiResponse(
            description="Autenticação bem-sucedida",
            response={
                "type": "object",
                "properties": {
                    "token": {"type": "string", "description": "Token de autenticação"},
                    "user": {"$ref": "#/components/schemas/User"},
                },
                "example": {
                    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
                    "user": {
                        "id": 1,
                        "username": "admin",
                        "email": "admin@example.com"
                    }
                }
            }
        ),
        400: OpenApiResponse(
            description="Dados inválidos",
            response={
                "type": "object",
                "example": {
                    "detail": "Campos username e password são obrigatórios"
                }
            }
        ),
        404: OpenApiResponse(
            description="Credenciais inválidas",
            response={
                "type": "object",
                "example": {
                    "detail": "Not found."
                }
            }
        ),
    },
    # Tags para organização no Swagger UI
    tags=["Autenticação"],
    # Exemplos adicionais
    examples=[
        OpenApiExample(
            "Exemplo de requisição",
            value={
                "username": "usuario_teste",
                "password": "senha_secreta"
            },
            request_only=True
        ),
        OpenApiExample(
            "Exemplo de resposta de sucesso",
            value={
                "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
                "user": {
                    "id": 2,
                    "username": "usuario_teste",
                    "email": "teste@example.com"
                }
            },
            response_only=True,
            status_codes=["200"]
        ),
    ]
)
@api_view(['POST'])
def login(request):
    """
       Autentica um usuário e retorna um token de acesso.

       Args:
           request (HttpRequest): Objeto de requisição contendo:
               - username (str): Nome de usuário
               - password (str): Senha do usuário

       Returns:
           Response: Contendo:
               - token (str): Token de autenticação
               - user (dict): Dados do usuário autenticado

       Raises:
           404: Se o usuário não existir ou a senha estiver incorreta
       """

    user = get_object_or_404(User, username= request.data['username'])#Verifica se existe
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

