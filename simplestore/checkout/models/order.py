from decimal import Decimal
import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse

from simplestore.cart.models import Cart
from simplestore.products.models.product import Product
from .address import Address
from .delivery import Delivery
from .payment import Payment


class Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=120, null=True, blank=True)
    status = models.CharField(choices=settings.ORDER_STATUS_CHOICES, max_length=120, default='Created')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='shipping_address',
                                         null=True)
    delivery_method = models.ForeignKey(Delivery, on_delete=models.DO_NOTHING, related_name='delivery_method',
                                        null=True)
    # payment_method = models.ForeignKey(Payment, on_delete=models.DO_NOTHING, related_name='payment_method', null=True)

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('checkout:order-confirmation', kwargs={'pk': self.pk})

    def create_order_items(self):
        cart_items = self.cart.items.all()
        for item in cart_items:
            OrderItem.objects.create(
                order=self,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity,
            )

    def __str__(self):
        return 'Order num. {0}'.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def get_total_price(self):
        return Decimal(self.price) * Decimal(self.quantity)

    def __str__(self):
        return 'Order item: {0} - {1}'.format(self.id, self.product.name)
