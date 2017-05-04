from .models import Cart


def get_cart(request, create=False):
    if not request.session.session_key:
        request.session.create()

    if request.user.is_authenticated() and request.session.get('user_cart'):
        kwargs = {'session_key': request.session['user_cart'], 'user': request.user}
    else:
        kwargs = {'session_key': request.session.session_key}

    try:
        return Cart.objects.get(**kwargs)
    except Cart.DoesNotExist:
        if create:
            return Cart.objects.create(**kwargs)
