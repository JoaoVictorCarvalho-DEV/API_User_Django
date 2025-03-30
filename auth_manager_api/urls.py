from django.urls import re_path
from .views.auth_view.registro import signup
from .views.auth_view.login import login
urlpatterns = [
re_path('login', login, name='login'),
re_path('signup', signup, name='register'),
# re_path('token', views.token, name='token'),
]
