"""Products views."""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Models
from subasta.products.models import Product


# Serializer
from subasta.products.serializers_public import ProductSerializer


@api_view(['GET'])
def list_products(request):
    """List products."""
    products   = Product.objects.filter(is_auctioned=False, is_active=True)
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data) 


# @api_view(['POST'])
# def create_product(request):
#     """Create producto."""

#     serializer = CreateProductSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     product = serializer.save()

#     return Response(ProductSerializer(product).data)