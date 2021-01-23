"""Sales URls."""


# Django
from django.urls import path, include


# Django REST Framework
from rest_framework.routers import DefaultRouter


# Views
from .views import sales as sale_views

router = DefaultRouter()
router.register(r'sales', sale_views.SaleViewSet, basename='sale')


urlpatterns = [
    path('', include(router.urls))
]
