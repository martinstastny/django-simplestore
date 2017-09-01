from django.db import models
from django.urls import reverse
from filer.fields.image import FilerImageField

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = FilerImageField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    _metadata = {
        'description': 'description',
    }

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('products:index', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name