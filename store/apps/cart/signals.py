from decimal import Decimal

# Signal before CartItem has been saved
def cart_item_pre_save_receiver(sender, instance, *args, **kwargs):
    if int(instance.quantity) >= 1:
        cart_item_total = Decimal(instance.quantity) * Decimal(instance.product.price)
        instance.total_price = cart_item_total

# Signal after CartItem has been saved
def cart_item_post_save_receiver(sender, instance, *args, **kwargs):
    instance.cart.update_subtotal()
    instance.cart.get_total_quantity_of_items()
