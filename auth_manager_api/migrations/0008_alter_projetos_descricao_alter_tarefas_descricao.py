# Generated by Django 5.1.7 on 2025-03-31 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_manager_api', '0007_rename_usuario_id_tarefas_responsavel_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarefas',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
