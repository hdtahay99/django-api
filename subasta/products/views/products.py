"""Products views."""

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from subasta.products.permissions.products import IsUserAdmin

# Serializers
from subasta.products.serializers import ProductModelSerializer


# Models
from subasta.products.models import Product


class ProductViewSet(mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Products view set."""

    queryset = Product.objects.filter(is_auctioned=False)
    serializer_class   = ProductModelSerializer
    permission_classes = (IsUserAdmin,)

    

    # def get_permissions(self):
    #     """Assign permissions based on action."""

    #     permissions = [IsAuthenticated]
    #     if self.action in ['list', 'create',' upadte', 'partial_update']:
    #         permissions.append()
    #     return [permission() for permission in permissions]



    # def get_queryset(self):
    #     """Restrict list to public-only."""

    #     queryset = Product.objects.filter(is_auctioned=False)
    #     if self.action == 'list':
    #         return queryset.filter(is_active=True)
    #     return queryset