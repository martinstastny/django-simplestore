from .models import Cart


def get_cart(request, create=False):
    """
    Return current Cart in session or create new Cart object if doesn't exists.
    :return: Cart object
    """
    if not request.session.session_key:
        request.session.create()

    if request.user.is_authenticated() and request.session.get('user_cart'):
        kwargs = {
            'session_key': request.session['user_cart'],
            'user': request.user
        }
    else:
        kwargs = {'session_key': request.session.session_key}

    try:
        return Cart.objects.get(**kwargs)
    except Cart.DoesNotExist:
        if create:
            return Cart.objects.create(**kwargs)
        else:
            return None
