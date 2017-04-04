from django.db import models
from cart.models import Cart
from profiles.models import Profile
from django.conf import settings


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    street = models.CharField(max_length=120, verbose_name='Address')
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    # address_type = models.CharField(choices=settings.ADDRESS_TYPE, max_length=120, default=None)
    zip_code = models.CharField(max_length=50)

    def __str__(self):
        return self.street


class Order(models.Model):
    cart = models.ForeignKey(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    email2 = models.EmailField(verbose_name='Email confirmation')
    phone = models.CharField(max_length=120)
    status = models.CharField(choices=settings.ORDER_STATUS_CHOICES, max_length=120)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # billing_address = models.ForeignKey(Address, related_name='billing_address')
    # shipping_address = models.ForeignKey(Address, related_name='shipping_address')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return 'Order num. {0}'.format(self.pk)