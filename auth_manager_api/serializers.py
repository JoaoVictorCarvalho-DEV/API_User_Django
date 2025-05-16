from rest_framework import serializers
from .models import CustomUser, Projetos, Tarefas, Orgaos, Atores, Mensagens

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = ['id','username', 'password', 'email', 'cpf', 'telefone', 'orgao_id', 'atores_id']


class TarefaSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Tarefas
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'data_inicio': {'format': '%d/%m/%Y'},
            'data_final': {'format': '%d/%m/%Y'}
        }


class MensagemSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta(object):
        model = Mensagens
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'projeto_id': {'read_only': True},
            'user_id': {'read_only': True}
        }


class ProjetoSerializer(serializers.ModelSerializer):
    tarefas = TarefaSerializer(many=True, read_only=True)

    mensagens = serializers.PrimaryKeyRelatedField(
        many= True,
        queryset= CustomUser.objects.all()
    )

    membros = serializers.PrimaryKeyRelatedField(
        many= True,
        queryset= CustomUser.objects.all()
    )

    class Meta(object):
        model = Projetos
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
        }


class OrgaoSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Orgaos
        fields = '__all__'
        extra_kwargs = {
            'id':{'read_only': True},
        }

class AtoresSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Atores
        fields = '__all__'
        extra_kwargs = {
            'id':{'read_only': True},
            'papel': {'read_only': True}
        }

