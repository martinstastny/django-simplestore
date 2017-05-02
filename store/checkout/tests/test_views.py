import datetime

from store.cart.mixins import get_cart
from store.cart.models import Cart, CartItem
from store.checkout.models.order import Order, OrderItem
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from django.urls import reverse
from store.products.models.product import Product

from store.profiles.models import Profile


class CheckoutTests(TestCase):
    def setUp(self):
        self.anonymous_user = AnonymousUser()

    @classmethod
    def setUpTestData(cls):
        # Product
        cls.test_product = Product(
            name='Testing Product',
            slug='testing-product',
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            price=1000,
            perex='Lorem ipsum',
            content='Lorem ipsum content',
        )

        cls.test_product.save()

    @staticmethod
    def _create_testing_cart(*args, **kwargs):
        cart = Cart(created=datetime.datetime.now(), updated=datetime.datetime.now(), *args, **kwargs)
        cart.save()

        return cart

    @staticmethod
    def _create_testing_cart_item(cart_instance, product_instance):
        cart_item = CartItem(cart=cart_instance, product=product_instance, quantity=1,
                             date_added=datetime.datetime.now())
        cart_item.save()

        return cart_item

    @staticmethod
    def _create_testing_order(cart, user):
        test_order = Order(
            cart=cart,
            user=user,
            full_name='Test Order Name',
            email='testemail@gmail.com',
            phone='744134567',
            status='created',
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        test_order.save()

        return test_order

    @staticmethod
    def _create_testing_user():
        user = Profile(
            email='vomacka@gmail.com',
            name='Martin',
            surname='Vomacka',
            slug='martin-vomacka',
            is_active=True,
            is_admin=False,
            is_staff=False,
        )
        user.set_password(raw_password='helloworld')
        user.save()

        return user

    '''
     Test when accessing /checkout url without items in cart will redirect back to cart
    '''
    def test_access_checkout_url_with_empty_cart(self):
        session = self.client.session
        request = self.client.get(reverse('checkout:index'))
        request.session = session
        request.user = self.anonymous_user

        cart = get_cart(request)
        cart_items_exists = cart.cartitem_set.exists()

        self.assertEqual(cart_items_exists, False, "Cart should not contain any items.")
        self.assertRedirects(request, reverse('cart:index'), 302, 200, "It should be redirected to cart index.")

    """
     Test if checkout is receiving Cart instance 
    """

    def test_cart_available_in_checkout(self):
        session = self.client.session

        test_cart = self._create_testing_cart()
        self._create_testing_cart_item(cart_instance=test_cart, product_instance=self.test_product)
        test_cart.session_key = session.session_key
        test_cart.save()

        r = self.client.get(reverse('checkout:index'))
        r.session = session
        r.user = self.anonymous_user

        self.assertEqual(r.context['cart'], test_cart)
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'checkout_index.html')

    """
     Test Order model string representation
    """

    def test_order_string_representation(self):
        test_cart = self._create_testing_cart()
        test_user = self._create_testing_user()

        test_order = self._create_testing_order(cart=test_cart, user=test_user)
        test_order.save()

        order_str = 'Order num. {0}'.format(test_order.pk)

        self.assertEqual(str(test_order), order_str)

    """
     Test Order Item string representation
    """

    def test_order_item_string_representation(self):
        test_user = self._create_testing_user()
        test_cart = self._create_testing_cart()
        test_cart.save()

        test_order = self._create_testing_order(cart=test_cart, user=test_user)
        test_order_item = OrderItem(
            order=test_order,
            product=self.test_product,
            price=self.test_product.price,
            quantity=1
        )

        test_order_item.save()

        self.assertEqual(str(test_order_item),
                         "Order item: {0} - {1}".format(test_order_item.id, test_order_item.product.name))

    def test_order_item_get_total_price(self):
        test_order_item = OrderItem(price=1000, quantity=4)
        total_price = test_order_item.get_total_price()

        self.assertEqual(total_price, 4000)