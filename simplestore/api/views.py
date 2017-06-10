from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from simplestore.products.models.product import Product
from simplestore.cart.models import CartItem
from simplestore.cart.mixins import get_cart
from . import serializers


class ProductListView(APIView):
    '''
    List all available active products
    '''

    def get(self, request, format=None):
        products = Product.objects.prefetch_related('image')
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data)


class CartDetailView(APIView):
    '''
    Cart detail view
    '''

    def get(self, request):
        cart = get_cart(request)
        serializer = serializers.CartSerializer(cart)
        return Response(serializer.data)


class CartUpdateDeleteView(APIView):
    '''
    Cart update view
    '''

    def get_object(self, id):
        try:
            cart = get_cart(self.request)
            return cart.items.get(pk=id)
        except CartItem.DoesNotExist:
            raise Http404


    def patch(self, request, id, *args, **kwargs):
        item = self.get_object(id)
        serializer = serializers.CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def delete(self, request, id):
        item = self.get_object(id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)