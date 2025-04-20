from django.urls import path, include
<<<<<<< HEAD
from .views import cadastrar_tarefa, ver_tarefas, editar_tarefa
=======
from .views import cadastrar_tarefa, ver_tarefas
>>>>>>> 87169d7dd057ed167690e8673e186c39b5725716

urlpatterns = [
    path('cadastrar_tarefa/', cadastrar_tarefa, name="cadastrar_tarefa"),
    path('ver_tarefas/', ver_tarefas, name="ver_tarefas"),
<<<<<<< HEAD
    path('editar-tarefa/<int:tarefa_id>/', editar_tarefa, name="editar_tarefa"),
=======
>>>>>>> 87169d7dd057ed167690e8673e186c39b5725716
]