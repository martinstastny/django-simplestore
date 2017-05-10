from django import template
from simplestore.cart.mixins import get_cart

register = template.Library()


@register.inclusion_tag('cart_counter.html', takes_context=True)
def cart_counter(context):
    request = context.get('request')
    cart = get_cart(request)
    qty = None

    if cart:
        qty = cart.get_total_quantity_of_items()

    return {
        'cart_items_total_qty': qty or 0
    }
