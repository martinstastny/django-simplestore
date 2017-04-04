from .models import Cart


def get_cart(request):
    if not request.session.session_key:
        request.session.create()

    if request.user.is_authenticated() and request.session.get('user_cart'):
        cart, created = Cart.objects.get_or_create(session_key=request.session['user_cart'],
                                                   user=request.user)
    else:
        cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)

    return cart
