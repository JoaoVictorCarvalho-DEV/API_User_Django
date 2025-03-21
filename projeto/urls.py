from django.contrib import admin
from django.urls import path
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api_project.urls')),
    path('sistema_auth/', include('sistema_auth.urls'))
]
