from django.db import models

class Payment(models.Model):
    name = models.CharField(max_length=125)

    class Meta:
        verbose_name = 'Payment Method'

    def __str__(self):
        return self.name