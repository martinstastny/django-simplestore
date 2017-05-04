from . import mixins


def cart_count_processor(request):
    cart = mixins.get_cart(request)
    if cart:
        cart_count = cart.get_total_quantity_of_items()
    else:
        cart_count = 0
    return {'cart_items_count': cart_count}
