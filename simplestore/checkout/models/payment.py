from django.db import models

import stripe
from simplestore.settings.base import STRIPE_PUBLIC_API_KEY

stripe.api_key = STRIPE_PUBLIC_API_KEY


class Payment(models.Model):
    name = models.CharField(max_length=125)

    class Meta:
        verbose_name = 'Payment Method'

    def __str__(self):
        return self.name