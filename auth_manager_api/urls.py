from django.urls import re_path

from .views.auth_view.registro import signup
from .views.auth_view.login import login

from .views.orgao_view.Listagem import OrgaoViewSet
from .views.projeto_view.Listagem import ProjetoViewSet
from .views.tarefa_view.Listagem import TarefaViewSet
from auth_manager_api.views.auth_view.Listagem import AtorViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('projetos', ProjetoViewSet)
router.register('tarefas', TarefaViewSet)
router.register('atores', AtorViewSet)
router.register('orgaos', OrgaoViewSet)

urlpatterns = [
re_path('login', login, name='login'),
re_path('signup', signup, name='register'),
# re_path('token', views.token, name='token'),
]
