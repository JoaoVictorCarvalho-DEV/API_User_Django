from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from auth_manager_api.serializers import UserSerializer
from auth_manager_api.models import CustomUser

from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiExample,
    OpenApiResponse,
    OpenApiRequest,
)


@extend_schema(
    # Configurações básicas
    summary="Atualização de usuário",
    description="""
    Endpoint para atualização parcial ou completa dos dados de um usuário existente.

    Funcionalidades especiais:
    - Atualização parcial (apenas campos enviados serão modificados)
    - Tratamento especial para campo 'password' (aplicação de hash automática)
    - Retorna os dados atualizados do usuário
    """,
    methods=["PUT"],
    tags=["Autenticação"],

    # Documentação dos parâmetros de URL
    parameters=[
        OpenApiParameter(
            name='user_id',
            type=int,
            location=OpenApiParameter.PATH,
            description='ID do usuário a ser atualizado',
            required=True,
        ),
    ],

    # Documentação do corpo da requisição
    request=UserSerializer,
    examples=[
        OpenApiExample(
            "Exemplo de atualização básica",
            value={
                "email": "novo_email@example.com",
                "first_name": "Novo Nome"
            },
            request_only=True
        ),
        OpenApiExample(
            "Exemplo com atualização de senha",
            value={
                "password": "novaSenhaSegura123",
                "last_name": "Novo Sobrenome"
            },
            request_only=True
        ),
    ],

    # Documentação das respostas
    responses={
        200: OpenApiResponse(
            description="Usuário atualizado com sucesso",
            response={
                "type": "object",
                "properties": {
                    "ok": {
                        "type": "string",
                        "example": "Usuário atualizado com sucesso",
                        "description": "Mensagem de confirmação"
                    },
                    "user": {
                        "$ref": "#/components/schemas/User",
                        "description": "Dados completos do usuário atualizado"
                    }
                }
            },
            examples=[
                OpenApiExample(
                    "Resposta de sucesso",
                    value={
                        "ok": "Usuário atualizado com sucesso",
                        "user": {
                            "id": 1,
                            "username": "usuario",
                            "email": "novo_email@example.com",
                            "first_name": "Novo Nome",
                            "last_name": "Novo Sobrenome"
                        }
                    }
                )
            ]
        ),
        400: OpenApiResponse(
            description="Dados inválidos",
            response={
                "type": "object",
                "example": {
                    "email": ["Insira um endereço de email válido."],
                    "username": ["Este campo é obrigatório."]
                }
            }
        ),
        404: OpenApiResponse(
            description="Usuário não encontrado",
            response={
                "type": "object",
                "example": {
                    "error": "Usuário não encontrado"
                }
            }
        ),
    }
)
@api_view(['PUT'])
def update(request, user_id):
    """
        Atualiza os dados de um usuário existente.

        Processo especial:
        - O campo 'password' recebe tratamento especial (hash automático)
        - Atualização parcial (apenas campos enviados são modificados)

        Args:
            request (HttpRequest): Pode conter qualquer campo do UserSerializer
            user_id (int): ID do usuário a ser atualizado

        Returns:
            Response: Em caso de sucesso (200), retorna:
                - ok (str): Mensagem de confirmação
                - user (dict): Dados atualizados do usuário
            Em caso de erro:
                - 400: Erros de validação dos dados
                - 404: Usuário não encontrado
        """
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({"error": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    # Se o campo 'password' foi enviado, trate ele separadamente
    password = request.data.get('password')

    # Serializa os outros dados (exceto a senha)
    serializer = UserSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        updated_user = serializer.save()

        # Se foi enviada uma nova senha, defina com hashing
        if password:
            updated_user.set_password(password)
            updated_user.save()

        return Response({
            "ok": "Usuário atualizado com sucesso",
            "user": UserSerializer(updated_user).data  # Re-serializa para refletir atualizações
        })

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

