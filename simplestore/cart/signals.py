from decimal import Decimal
from simplestore.cart.models import Cart


def cart_item_pre_save_receiver(sender, instance, *args, **kwargs):
    if int(instance.quantity) >= 1:
        cart_item_total = Decimal(instance.quantity) * Decimal(instance.product.price)
        instance.total_price = cart_item_total

# Signal after CartItem has been saved
def cart_item_post_save_receiver(sender, instance, *args, **kwargs):
    try:
        cart = instance.cart
    except Cart.DoesNotExist:
        pass
    else:
        cart.update_subtotal()
