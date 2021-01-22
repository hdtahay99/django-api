"""Offers views."""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Models
from subasta.offers.models import Offer
from subasta.products.models import Product


# Serializer
from subasta.offers.serializers import OfferModelSerializer, CreateOfferSerializer


@api_view(['POST'])
def create_offer(request):
    """Create product offer."""


    product = Product.objects.get(id=request.data.get('product'))
    print(type(product))
    nuevo = Offer.objects.create(
        user=request.user,
        product=product,
        price_offer=request.data.get('price_offer')
    )

    return Response(OfferModelSerializer(nuevo).data)