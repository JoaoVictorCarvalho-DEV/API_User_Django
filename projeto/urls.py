<<<<<<< HEAD
from django.contrib import admin
from django.urls import path
from django.urls import include
from auth_manager_api.urls import router
urlpatterns = [
    path('admin/', admin.site.urls),
    #####SERVIÇOS#####
    path('site/auth/', include('sistema_auth.urls')),#Essas são as URLs principais
    path('site/projetos/', include("projeto_service.urls")),
    path('site/tarefas/', include("tarefa_service.urls")),
    path('site/atores/', include("atores_service.urls")),
    path('site/orgaos/', include("orgao_service.urls")),

    #####API#####
    path('auth_api/', include('auth_manager_api.urls')),#URLS da API

    path('api/v1/', include(router.urls))

]
=======
from django.contrib import admin
from django.urls import path
from django.urls import include
from auth_manager_api.urls import router
urlpatterns = [
    path('admin/', admin.site.urls),
    #####SERVIÇOS#####
    path('site/auth/', include('sistema_auth.urls')),#Essas são as URLs principais
    path('site/projetos/', include("projeto_service.urls")),
    path('site/tarefas/', include("tarefa_service.urls")),
    path('site/atores/', include("atores_service.urls")),

    #####API#####
    path('auth_api/', include('auth_manager_api.urls')),#URLS da API

    path('api/v1/', include(router.urls))

]
>>>>>>> 87169d7dd057ed167690e8673e186c39b5725716
