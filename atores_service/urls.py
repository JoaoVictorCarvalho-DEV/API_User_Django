from django.urls import path, include
from .views import cadastrar_ator, ver_atores, editar_ator

urlpatterns = [
    path('cadastrar_ator/',cadastrar_ator, name="cadastrar_ator"),
    path('ver_ator/',ver_atores, name="ver_atores"),
    path('editar_ator/',editar_ator, name="editar_ator"),
]