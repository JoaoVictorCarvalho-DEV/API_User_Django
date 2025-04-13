from django.urls import path, include
from .views import cadastrar_projeto, ver_projetos, editar_projeto, ver_projeto

urlpatterns = [
    path('cadastrar-projeto/', cadastrar_projeto, name="cadastrar_projeto"),

    path('editar-projeto/<int:projeto_id>/', editar_projeto, name="editar_projeto"),
    path('ver-projetos/', ver_projetos, name="ver_projetos"),
    path('ver-projeto/<int:projeto_id>/', ver_projeto, name="ver_projeto"),
]