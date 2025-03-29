from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Orgaos)
class OrgaoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'sigla'
    )

@admin.register(Atores)
class AtoresAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'papel'
    )

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomUser._meta.fields]


@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Projetos._meta.fields]


@admin.register(Tarefas)
class TarefasAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tarefas._meta.fields]