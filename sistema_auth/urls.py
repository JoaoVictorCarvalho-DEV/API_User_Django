from django.contrib import admin
from django.urls import path, include
from .views import  login_view, dashboard, logout_view, register

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registro/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout')
]