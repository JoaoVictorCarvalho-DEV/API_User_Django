from django.contrib import admin
from django.urls import path, include
from .views import  login_api, registro_api, dash_api

urlpatterns = [
    # path('login/', login_view, name='login'),
    # path('registro/', register, name='register'),
    # path('dashboard/', dashboard, name='dashboard'),
    # path('logout/', logout_view, name='logout'),
    path('login_api/', login_api, name='login_api'),
    path('registro_api/', registro_api, name='register_api'),
    path('dashboard_api/', dash_api, name='dashboard_api'),

]