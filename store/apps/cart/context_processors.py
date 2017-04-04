from . import mixins


def cart_count_processor(request):
    cart = mixins.get_cart(request)
    cart_count = cart.get_total_quantity_of_items()
    return {'cart_items_count': cart_count if cart else 0}
