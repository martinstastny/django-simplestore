from django.db import models
from cart.models import Cart
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
        ordering = ['-id']

    def __str__(self):
        return 'Order num. {0}'.format(self.pk)