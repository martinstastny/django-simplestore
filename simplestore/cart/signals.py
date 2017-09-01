from decimal import Decimal

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Cart, CartItem


@receiver(pre_save, sender=CartItem)
def cart_item_pre_save_receiver(sender, instance, *args, **kwargs):
    if int(instance.quantity) >= 1:
        cart_item_total = Decimal(instance.quantity) * Decimal(
            instance.product.price)
        instance.total_price = cart_item_total


@receiver(post_save, sender=CartItem)
def cart_item_post_save_receiver(sender, instance, *args, **kwargs):
    try:
        cart = instance.cart
    except Cart.DoesNotExist:
        pass
    else:
        cart.update_subtotal()
