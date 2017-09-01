from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver

from .models.product import Product


@receiver(pre_delete, sender=Product)
def product_pre_delete_receiver(sender, instance, **kwargs):
    """Instead of deleting object from DB set it's state is_active to False"""
    instance.is_active = False


@receiver(post_delete, sender=Product)
def product_post_delete_receiver(sender, instance, **kwargs):
    """Save changed state of instance"""
    instance.save()
