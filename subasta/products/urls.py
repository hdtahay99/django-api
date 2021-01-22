"""Products URls."""


# Django
from django.urls import path, include


# Django REST Framework
from rest_framework.routers import DefaultRouter


# Views
from .views import products as product_views
from subasta.products.views_public import list_products

router = DefaultRouter()
router.register(r'products', product_views.ProductViewSet, basename='product')


urlpatterns = [
    path('products/public/', list_products),
    path('', include(router.urls))
]
