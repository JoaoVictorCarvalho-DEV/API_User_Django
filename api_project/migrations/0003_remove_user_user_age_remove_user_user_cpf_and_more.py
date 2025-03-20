# Generated by Django 5.1.7 on 2025-03-20 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_project', '0002_user_id_alter_user_user_cpf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_cpf',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_telephone',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='cpf',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='telephone',
            field=models.IntegerField(default=0),
        ),
    ]
