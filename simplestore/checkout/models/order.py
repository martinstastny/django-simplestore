from decimal import Decimal
from uuid import uuid4

from django.conf import settings
from django.db import models
from django.urls import reverse

from simplestore.cart.models import Cart
from simplestore.products.models.product import Product
from .address import Address

# Orders Statuses
ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('in_progress', 'In Progress'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('canceled', 'Cancelled'),
)


class Order(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True, editable=False)
    slug = models.UUIDField(default=uuid4, unique=True, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=120, null=True, blank=True)
    status = models.CharField(choices=ORDER_STATUS_CHOICES, max_length=120, default='Created')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='shipping_address',
        null=True)

    class Meta:
        ordering = ['-created_at']

    def get_short_uuid(self):
        uuid = str(self.uuid).split('-')
        return "{0}-{1}".format(uuid[0], uuid[1])

    def get_cart_items(self):
        return self.cart.items.all()

    def get_absolute_url(self):
        return reverse('checkout:order-confirmation', kwargs={'slug': str(self.slug)})

    def create_order_items(self):
        cart_items = self.cart.items.all()
        for item in cart_items:
            OrderItem.objects.create(order=self, product=item.product, price=item.product.price,
                quantity=item.quantity)

    def get_serialized_items(self):
        order_items = []
        for item in self.cart.items.all():
            data = {
                'name': item.product.name,
                'sku': item.product.sku,
                'quantity': item.quantity,
                'price': item.product.price,
                'total_price': item.total_price,
            }
            order_items.append(data)
        return order_items

    def get_serialized_data(self):
        return {
            'short_uuid': self.get_short_uuid(),
            'email': self.email,
            'full_name': self.full_name,
            'phone': self.phone,
            'status': self.status,
            'shipping_address': self.shipping_address,
            'order_items': self.get_serialized_items(),
        }

    def __str__(self):
        return 'Order num. {0}'.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def get_total_price(self):
        return Decimal(self.price) * Decimal(self.quantity)

    def __str__(self):
        return 'Order item: {0} - {1}'.format(self.id, self.product.name)
