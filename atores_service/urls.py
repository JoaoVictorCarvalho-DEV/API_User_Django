from django.urls import path, include
from .views import cadastrar_ator, ver_atores, editar_ator, ver_ator

urlpatterns = [
    path('cadastrar_ator/',cadastrar_ator, name="cadastrar_ator"),
    path('ver_ator/<int:user_id>/',ver_ator, name="ver_ator"),
    path('editar_ator/<int:user_id>/',editar_ator, name="editar_ator"),
    path('', ver_atores, name="ver_atores")
]