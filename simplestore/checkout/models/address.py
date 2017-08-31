from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=25)
    country = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Addresses'

    def get_serialized_data(self):
        return {
            'street': self.street,
            'city': self.city,
            'postcode': self.postcode,
            'country': self.country
        }

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.street, self.city, self.country)
