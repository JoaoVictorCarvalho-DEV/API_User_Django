from django.urls import path, include
from .views import cadastrar_tarefa, ver_tarefas, editar_tarefa

urlpatterns = [
    path('cadastrar_tarefa/', cadastrar_tarefa, name="cadastrar_tarefa"),
    path('ver_tarefas/', ver_tarefas, name="ver_tarefas"),
    path('editar-tarefa/<int:tarefa_id>/', editar_tarefa, name="editar_tarefa"),
]