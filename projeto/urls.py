from django.contrib import admin
from django.urls import path
from django.urls import include
urlpatterns = [
    path('admin', admin.site.urls),
    path('sistema_auth', include('sistema_auth.urls')),

    path('auth_api', include('auth_manager_api.urls'))
]
