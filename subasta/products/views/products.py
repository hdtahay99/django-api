"""Products views."""

# Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from subasta.products.serializers import ProductModelSerializer


# Models
from subasta.products.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """Products view set."""

    queryset = Product.objects.filter(is_auctioned=False)
    serializer_class   = ProductModelSerializer
    permission_classes = (IsAuthenticated,)


    # def get_queryset(self):
    #     """Restrict list to public-only."""

    #     queryset = Product.objects.filter(is_auctioned=False)
    #     if self.action == 'list':
    #         return queryset.filter(is_active=True)
    #     return queryset