from _decimal import Decimal

from django.db import models
from cart.models import Cart
from products.models.product import Product
from profiles.models import Profile
from django.conf import settings


class Order(models.Model):
    cart = models.ForeignKey(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=120, null=True)
    status = models.CharField(choices=settings.ORDER_STATUS_CHOICES, max_length=120)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return 'Order num. {0}'.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return Decimal(self.price) * Decimal(self.quantity)

    def __str__(self):
        return 'Order ID: {0} - {1}'.format(self.id, self.product.name)
