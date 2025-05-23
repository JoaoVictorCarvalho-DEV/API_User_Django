from django.urls import path, include

from .views import ver_dashboard

urlpatterns = [
path('',ver_dashboard, name="ver_dashboard")
]