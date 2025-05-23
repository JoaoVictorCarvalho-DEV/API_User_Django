from django.urls import re_path, path

from .views.auth_view.registro import signup
from .views.auth_view.login import login
from .views.auth_view.update import update

from .views.orgao_view.Listagem import OrgaoViewSet
from .views.projeto_view.Listagem import ProjetoViewSet
from .views.tarefa_view.Listagem import TarefaViewSet
from auth_manager_api.views.auth_view.Listagem import AtorViewSet,PapelViewSet

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('projetos', ProjetoViewSet)
router.register('tarefas', TarefaViewSet)
router.register('atores', AtorViewSet)
router.register('papel', PapelViewSet)
router.register('orgaos', OrgaoViewSet)

urlpatterns = [
path('login', login, name='login'),
path('signup', signup, name='register'),
path('update/<int:user_id>', update, name='update'),
path('schema/', SpectacularAPIView.as_view(), name='schema'),
path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
