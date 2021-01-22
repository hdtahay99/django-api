"""Offers views."""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Models
from subasta.offers.models import Offer
from subasta.products.models import Product


# Serializer
from subasta.offers.serializers import OfferModelSerializer, CreateOfferSerializer




@api_view(['POST'])
def create_offer(request):
    """Create product offer."""

    product = Product.objects.get(id=request.data.get('product'))
    if hasattr(request.user, 'is_client'):
        if request.user.is_client == True and product.is_auctioned == False and product.is_active == True:
            nuevo = Offer.objects.create(
                user=request.user,
                product=product,
                price_offer=request.data.get('price_offer')
            )

            return Response(OfferModelSerializer(nuevo).data)
        else:
            return Response({'error' : 'Please, comunicated with de administrator, the user is not permited or the product already auctioned'}, status=status.HTTP_423_LOCKED)
    else:
        return Response({'error' : 'Please, comunicated with de administrator, the user is not permited'}, status=status.HTTP_403_FORBIDDEN)



@api_view(['GET'])
def list_offer_product(request):
    """List the products's offer"""
    
    if hasattr(request.user, 'is_client'):
        if request.user.is_admin == True:
            products_offereds = Offer.objects.select_related('product').values('user','product', 'price_offer')
            return Response(products_offereds)
        else:
            return Response({'error' : 'Please, comunicated with de administrator, the user is not permited'}, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response({'error' : 'Please, comunicated with de administrator, the user is not permited'}, status=status.HTTP_403_FORBIDDEN)



@api_view(['GET'])
def list_offers_product(request):
    """List the the product's offers"""

    if hasattr(request.user, 'is_client'):
        if request.user.is_client == True:
            products_offereds = Offer.objects.filter(product=request.data.get('product')).select_related('product').values('user','product', 'price_offer')
            return Response(products_offereds)
        else:
            return Response({'error' : 'Please, comunicated with de administrator, the user is not permited'}, status=status.HTTP_403_FORBIDDEN)    
    else:
        return Response({'error' : 'Please, comunicated with de administrator, the user is not permited'}, status=status.HTTP_403_FORBIDDEN)


