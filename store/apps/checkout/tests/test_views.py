from django.test import TestCase
from django.urls import reverse
from cart.mixins import get_cart
from django.contrib.auth.models import AnonymousUser


class CheckoutTests(TestCase):

    def setUp(self):
        self.anonymous_user = AnonymousUser()

    """
     Test when accessing /checkout url without items in cart will redirect back to cart
    """
    def test_access_checkout_url_with_empty_cart(self):
        session = self.client.session
        request = self.client.get(reverse('checkout:index'))
        request.session = session
        request.user = self.anonymous_user

        cart = get_cart(request)
        cart_items_exists = cart.cartitem_set.exists()

        self.assertEqual(cart_items_exists, False, "Cart should not contains any items.")
        self.assertRedirects(request,reverse('cart:index'), 302, 200, "It should be redirected to cart index.")

