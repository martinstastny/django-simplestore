from django.conf import settings
from django.db import models

from simplestore.products.models.product import Product


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    session_key = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    price_subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    price_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        unique_together = ('user', 'session_key')

    def update_subtotal(self):
        subtotal = self.items.all().aggregate(sum=models.Sum('total_price'))
        self.price_subtotal = subtotal['sum']
        self.save()

    def get_total_quantity_of_items(self):
        qty = self.items.all().aggregate(sum=models.Sum('quantity'))
        return qty['sum']

    def __str__(self):
        return "Cart id: {id}".format(id=self.pk)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, related_name='items', blank=True)
    product = models.ForeignKey(Product, related_name='products', on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        ordering = ['date_added']

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def __str__(self):
        return self.product.name
