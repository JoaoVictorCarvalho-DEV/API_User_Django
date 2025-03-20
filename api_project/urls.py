from django.contrib import admin
from django.urls import path, include
from .views import UserApiView, UsersApiView, lista_user, register, login_view, dashboard, logout_view

urlpatterns = [
    path('listar/', UsersApiView.as_view(), name='get_all_users'),
    path('listar/<int:pk>', UserApiView.as_view(), name='get_one'),
    path('login/', login_view, name='login'),
    path('registro/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout')
]