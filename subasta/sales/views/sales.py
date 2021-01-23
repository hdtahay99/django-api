"""Sales views."""

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from subasta.sales.permissions.sales import IsUserAdmin
from rest_framework.response import Response

# Serializers
from subasta.sales.serializers import SaleModelSerializer


# Models
from subasta.sales.models import Sale
from subasta.products.models import Product
from subasta.offers.models import Offer


class SaleViewSet(mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Sales view set."""

    queryset = Sale.objects.all()
    serializer_class   = SaleModelSerializer
    permission_classes = (IsUserAdmin,)


    def perfom_create(self, serializer):
        """Update the product."""
        offer   = Offer.objects.get(id=request.data['offer'])
        Product.objects.filter(id = offer.product.id).update(is_auctioned = True)
        sale = serializer.save()
