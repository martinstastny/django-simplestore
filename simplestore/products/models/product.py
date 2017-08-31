from django.core.urlresolvers import reverse
from django.db import models
from filer.fields.image import FilerImageField

from .category import Category


class ProductQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self.db)

    def all(self):
        return self.get_queryset().active()


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    sku = models.CharField(
        max_length=50,
        verbose_name='Reference Number',
        unique=True
    )
    created_at = models.DateTimeField(auto_now=True, db_index=True)
    updated_at = models.DateTimeField(auto_now_add=True, db_index=True)
    image = FilerImageField(null=True, blank=True, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    perex = models.TextField(max_length=255)
    content = models.TextField(verbose_name='Content Description')
    category = models.ManyToManyField(Category, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_featured = models.BooleanField(default=False, verbose_name='Featured')

    objects = ProductManager()

    _metadata = {
        'description': 'content',
    }

    class Meta:
        ordering = ['-created_at']

    @property
    def get_image_url(self):
        return self.image.url

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
