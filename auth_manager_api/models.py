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
    atores_id = models.ForeignKey(Atores, on_delete=models.SET_NULL, null=True, blank=True)
    orgao_id  = models.ForeignKey(Orgaos, on_delete=models.SET_NULL, null=True, blank=True)

    REQUIRED_FIELDS = ['email', 'cpf']

    def __str__(self):
        return self.username
    


class Projetos(models.Model):
    class Meta:
        db_table = "projetos"
    
    nome = models.CharField(max_length=50, null=False)
    descricao = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_final = models.DateField()
    projeto_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    atores_id = models.ForeignKey(Atores, on_delete=models.SET_NULL, null=True, blank=True)

class Tarefas(models.Model):
    class Meta:
        db_table = "tarefas"

    nome = models.CharField(max_length=50, null=False)
    descricao = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_final = models.DateField()
    usuario_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    orgao_id = models.ForeignKey(Orgaos, on_delete=models.SET_NULL, null=True, blank=True)

