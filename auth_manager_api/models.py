from django.contrib.auth import get_user_model
from django.db import models

from django.contrib.auth.models import AbstractUser




# Create your models here.
class Atores(models.Model):
    class Meta:
        db_table = "atores"

    papel = models.CharField(max_length=50)

class Orgaos(models.Model):
    class Meta:
        db_table = "orgaos"
    
    nome = models.CharField(max_length=255, null=False)
    sigla = models.CharField(max_length=10)


class CustomUser(AbstractUser):
    class Meta:
        db_table ="users"

    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    atores_id = models.ForeignKey(Atores, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_ator')
    orgao_id  = models.ForeignKey(Orgaos, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_orgao')

    REQUIRED_FIELDS = ['email', 'cpf']

    def __str__(self):
        return self.username
    
User = get_user_model()

class Projetos(models.Model):
    class Meta:
        db_table = "projetos"
    
    nome = models.CharField(max_length=50, null=False)
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateField()
    data_final = models.DateField()
    status = models.CharField(max_length=50, null=False, default="Em andamento")
    orgao_id = models.ForeignKey(Orgaos, on_delete=models.SET_NULL, null=True, blank=True, related_name='proj_orgao')
    analista_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='proj_analista')
    desenvolvedor_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='proj_desenvolvedor')
    membros = models.ManyToManyField(CustomUser, related_name='projetos_participando', blank=True)


class Tarefas(models.Model):
    class Meta:
        db_table = "tarefas"

    nome = models.CharField(max_length=50, null=False)
    descricao = models.TextField(blank=True, null=True)
    projeto_id = models.ForeignKey(Projetos, on_delete=models.CASCADE, null=True, blank=True, related_name='tarefas')
    status = models.CharField(max_length=50,null=False, default="Em andamento")
    data_inicio = models.DateField()
    data_final = models.DateField()
    responsavel_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarefa_responsavel')
    orgao_id = models.ForeignKey(Orgaos, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarefa_orgao')

class Mensagens(models.Model):
    projeto_id = models.ForeignKey(Projetos, on_delete=models.CASCADE, related_name='mensagens')
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)