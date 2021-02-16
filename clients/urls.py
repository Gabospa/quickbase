""" Client URLs."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from . import views

router = DefaultRouter()
router.register(r'clients', views.ClientViewSet, basename='clients')


urlpatterns = [
    path('clients/read/', views.read_csv),
    path('', include(router.urls))
]