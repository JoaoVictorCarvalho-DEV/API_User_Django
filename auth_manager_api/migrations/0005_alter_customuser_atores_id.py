# Generated by Django 5.1.7 on 2025-03-29 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_manager_api', '0004_alter_customuser_orgao_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='atores_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth_manager_api.atores'),
        ),
    ]
