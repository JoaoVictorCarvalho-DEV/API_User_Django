from django.urls import path, include
<<<<<<< HEAD
from .views import cadastrar_projeto, ver_projetos, editar_projeto, ver_projeto
=======
from .views import cadastrar_projeto, ver_projetos, editar_projeto
>>>>>>> 87169d7dd057ed167690e8673e186c39b5725716

urlpatterns = [
    path('cadastrar-projeto/', cadastrar_projeto, name="cadastrar_projeto"),

    path('editar-projeto/<int:projeto_id>/', editar_projeto, name="editar_projeto"),
    path('ver-projetos/', ver_projetos, name="ver_projetos"),
<<<<<<< HEAD
    path('ver-projeto/<int:projeto_id>/', ver_projeto, name="ver_projeto"),
=======
>>>>>>> 87169d7dd057ed167690e8673e186c39b5725716
]