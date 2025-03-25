from django.urls import re_path
from . import views

urlpatterns = [
re_path('login', views.login, name='login'),
re_path('signup', views.signup, name='register'),
re_path('token', views.token, name='token'),
]
