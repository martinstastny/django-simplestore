from decimal import Decimal
from django.db import models
from products.models.product import Product
from django.conf import settings


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    price_subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    session_key = models.CharField(max_length=255, null=True)

    class Meta:
        unique_together = ('user', 'session_key')

    def update_subtotal(self):
        items = self.cartitem_set.all()
        subtotal = 0
        for item in items:
            subtotal += Decimal(item.total_price)
        self.price_subtotal = subtotal
        self.save()

    def get_total_quantity_of_items(self):
        items = self.cartitem_set.all()
        return sum(item.quantity for item in items)

    def __str__(self):
        return "Cart id: {id}".format(id=self.pk)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        ordering = ['date_added']

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def __str__(self):
        return self.product.name