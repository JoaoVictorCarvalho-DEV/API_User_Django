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
<<<<<<< HEAD
    atores_id = models.ForeignKey(Atores, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_ator')
    orgao_id  = models.ForeignKey(Orgaos, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_orgao')
=======
    atores_id = models.ForeignKey(Atores, on_delete=models.SET_NULL, null=True, blank=True)
    orgao_id  = models.ForeignKey(Orgaos, on_delete=models.SET_NULL, null=True, blank=True)
>>>>>>> 87169d7dd057ed167690e8673e186c39b5725716

    REQUIRED_FIELDS = ['email', 'cpf']

    def __str__(self):
        return self.username
    


class Projetos(models.Model):
    class Meta:
        db_table = "projetos"
    
    nome = models.CharField(max_length=50, null=False)
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateField()
    data_final = models.DateField()
<<<<<<< HEAD
    orgao_id = models.ForeignKey(Orgaos, on_delete=models.SET_NULL, null=True, blank=True, related_name='proj_orgao')
=======
    orgao_id = models.ForeignKey(Orgaos, on_delete=models.SET_NULL, null=True, blank=True)
>>>>>>> 87169d7dd057ed167690e8673e186c39b5725716
    analista_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='proj_analista')
    desenvolvedor_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='proj_desenvolvedor')

class Tarefas(models.Model):
    class Meta:
        db_table = "tarefas"

    nome = models.CharField(max_length=50, null=False)
    descricao = models.TextField(blank=True, null=True)
    projeto_id = models.ForeignKey(Projetos, on_delete=models.CASCADE, null=True, blank=True, related_name='tarefas')
    data_inicio = models.DateField()
    data_final = models.DateField()
<<<<<<< HEAD
    responsavel_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarefa_responsavel')
    orgao_id = models.ForeignKey(Orgaos, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarefa_orgao')
=======
    responsavel_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    orgao_id = models.ForeignKey(Orgaos, on_delete=models.SET_NULL, null=True, blank=True)
>>>>>>> 87169d7dd057ed167690e8673e186c39b5725716

