from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from simplestore.cart.models import CartItem
from simplestore.cart.utils import get_cart
from simplestore.products.models.product import Product
from . import serializers


class ProductListView(APIView):
    def get(self, request):
        """
        List all available active products 
        """
        products = Product.objects.prefetch_related('image')
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data)


class CartDetailView(APIView):
    def get(self, request):
        """
        Cart detail view 
        """
        cart = get_cart(request)
        serializer = serializers.CartSerializer(cart)
        return Response(serializer.data)


class CartUpdateDeleteView(APIView):
    def get_object(self, cart_id):
        """
        Cart update view 
        """
        try:
            cart = get_cart(self.request)
            return cart.items.get(pk=cart_id)
        except CartItem.DoesNotExist:
            raise Http404

    def patch(self, request, product_id):
        item = self.get_object(product_id)
        serializer = serializers.CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, product_id):
        item = self.get_object(product_id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
