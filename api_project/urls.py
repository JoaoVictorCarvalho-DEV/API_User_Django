from django.contrib import admin
from django.urls import path, include
from .views import UserApiView, UsersApiView

urlpatterns = [
    path('listar/', UsersApiView.as_view(), name='get_all_users'),
    path('listar/<int:pk>', UserApiView.as_view(), name='get_one_user'),

]