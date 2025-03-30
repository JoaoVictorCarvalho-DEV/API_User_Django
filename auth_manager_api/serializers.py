from rest_framework import serializers
from .models import CustomUser, Projetos, Tarefas, Orgaos, Atores

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = ['id','username', 'password', 'email', 'cpf', 'telefone']


class ProjetoSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Projetos
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'data_inicio': {'format': '%d/%m/%Y'},
            'data_final': {'format': '%d/%m/%Y'}
        }

class TarefaSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Tarefas
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'data_inicio': {'format': '%d/%m/%Y'},
            'data_final': {'format': '%d/%m/%Y'}
        }

class OrgaoSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Orgaos
        fields = '__all__'
        extra_kwargs = {
            'id':{'ready_only': True},
        }

class AtoresSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Atores
        fields = '__all__'
        extra_kwargs = {
            'id':{'read_only': True},
            'papel': {'read_only': True}
        }