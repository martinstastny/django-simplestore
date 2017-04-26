from django.db import models

class Delivery(models.Model):
    name = models.CharField(max_length=125)
    price = models.PositiveIntegerField(default=0)
    delivery_time = models.TextField(max_length=255)

    class Meta:
        verbose_name = 'Delivery Method'

    def __str__(self):
        return self.name