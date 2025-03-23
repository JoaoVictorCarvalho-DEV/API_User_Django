from django.contrib import admin
from django.urls import path
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('site/', include('sistema_auth.urls')),#Essas são as URLs principais

    path('auth_api/', include('auth_manager_api.urls'))#URLS da API
]
