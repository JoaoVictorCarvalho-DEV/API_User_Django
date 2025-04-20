from django.urls import path, include
from .views import cadastrar_ator, ver_atores

urlpatterns = [
    path('cadastrar_ator/',cadastrar_ator, name="cadastrar_ator"),
<<<<<<< HEAD
    path('ver_ator/',ver_atores, name="ver_atores"),
=======
path('ver_ator/',ver_atores, name="ver_atores"),
>>>>>>> 87169d7dd057ed167690e8673e186c39b5725716
]