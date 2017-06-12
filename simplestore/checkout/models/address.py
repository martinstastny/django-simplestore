from django.db import models

ADDRESS_TYPES = (
    ('shipping', 'Shipping'),
    ('billing', 'Billing')
)

class Address(models.Model):
    # address_type = models.CharField(choices=ADDRESS_TYPES, max_length=120)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=25)
    country = models.CharField(max_length=255)
    # use_as_billing = models.BooleanField(default=True, verbose_name='Use shipping address as billing address')

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.street, self.city, self.country)