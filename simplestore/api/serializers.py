from rest_framework import serializers
from simplestore.products.models.product import Product
from simplestore.cart.models import Cart, CartItem


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SlugField(source='get_image_url', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'perex', 'image', 'created_at', 'content',)


class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id')
    name = serializers.StringRelatedField(source='product.name')
    price = serializers.StringRelatedField(source='product.price')
    perex = serializers.StringRelatedField(source='product.perex')
    image = serializers.SlugField(source='product.get_image_url')
    url = serializers.SlugField(source='product.get_absolute_url')

    class Meta:
        model = CartItem
        fields = (
            'id',
            'name',
            'product_id',
            'image',
            'url',
            'perex',
            'date_added',
            'price',
            'quantity',
            'total_price',
        )


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'price_total', 'price_subtotal', 'created', 'items')
