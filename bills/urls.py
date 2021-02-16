""" Bill URLs."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from . import views

router = DefaultRouter()
router.register(r'bills', views.BillViewSet, basename='bills')
router.register(r'bills-products', views.BillProductsViewSet, basename='bills-products')

urlpatterns = [
    path('', include(router.urls))
]