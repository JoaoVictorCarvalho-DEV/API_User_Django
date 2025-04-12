# Generated by Django 5.1.7 on 2025-04-04 15:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_manager_api', '0008_alter_projetos_descricao_alter_tarefas_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='atores_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ator', to='auth_manager_api.atores'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='orgao_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_orgao', to='auth_manager_api.orgaos'),
        ),
        migrations.AlterField(
            model_name='projetos',
            name='orgao_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proj_orgao', to='auth_manager_api.orgaos'),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='orgao_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tarefa_orgao', to='auth_manager_api.orgaos'),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='projeto_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to='auth_manager_api.projetos'),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='responsavel_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tarefa_responsavel', to=settings.AUTH_USER_MODEL),
        ),
    ]
