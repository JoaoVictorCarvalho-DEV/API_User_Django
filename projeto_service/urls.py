from django.urls import path, include
from .views import cadastrar_projeto, ver_projetos

urlpatterns = [
    path('cadastrar-projeto/', cadastrar_projeto, name="cadastrar_projeto"),
    path('ver-projetos/', ver_projetos, name="ver_projetos"),
]