from django.urls import path, include
from .views import ver_orgaos, cadastrar_orgao, editar_orgao

urlpatterns = [
    path('cadastrar-orgao/', cadastrar_orgao, name="cadastrar_orgao"),

    path('editar-orgao/<int:projeto_id>/', editar_orgao, name="editar_orgao"),
    path('ver-orgaos/', ver_orgaos, name="ver_orgaos"),
]