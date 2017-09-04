from decimal import Decimal

from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from .models import CartItem


@receiver(pre_save, sender=CartItem)
def cart_item_pre_save_receiver(sender, instance, **kwargs):
    if int(instance.quantity) >= 1:
        cart_item_total = Decimal(instance.quantity) * Decimal(instance.product.price)
        instance.total_price = cart_item_total


@receiver(post_save, sender=CartItem)
def cart_item_post_save_receiver(sender, instance, **kwargs):
    instance.cart.update_subtotal()


@receiver(post_delete, sender=CartItem)
def cart_item_post_delete_receiver(sender, instance, **kwargs):
    instance.cart.update_subtotal()
