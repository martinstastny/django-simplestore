from rest_framework.views import APIView
from rest_framework.response import Response

from simplestore.products.models.product import Product
from simplestore.cart.mixins import get_cart
from .serializers import ProductSerializer, CartSerializer


class ProductListView(APIView):
    '''
    List all available active products
    '''

    def get(self, request, format=None):
        products = Product.objects.prefetch_related('image')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class CartView(APIView):
    '''
    Cart detail view
    '''

    def get(self, request):
        cart = get_cart(request)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
