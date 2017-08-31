import datetime

from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from django.urls import reverse

from simplestore.cart.models import Cart, CartItem
from simplestore.cart.utils import get_cart
from simplestore.checkout.models.order import Order, OrderItem
from simplestore.products.models.product import Product
from simplestore.profiles.models import Profile


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
        cart = Cart(
            created=datetime.datetime.now(),
            updated=datetime.datetime.now(), *args, **kwargs
        )
        cart.save()

        return cart

    @staticmethod
    def _create_testing_cart_item(cart_instance, product_instance):
        cart_item = CartItem(
            cart=cart_instance,
            product=product_instance,
            quantity=1,
            date_added=datetime.datetime.now()
        )
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

    def test_access_checkout_url_with_empty_cart(self):
        """
         Test when accessing /checkout url without items in cart will 
         redirect back to cart
        """
        session = self.client.session
        request = self.client.get(reverse('checkout:index'))
        request.session = session
        request.user = self.anonymous_user

        cart = get_cart(request)

        self.assertEqual(cart, None, "Cart should not exists")
        self.assertRedirects(
            request,
            reverse('cart:index'), 302, 200,
            "It should be redirected to cart index."
        )

    def test_cart_available_in_checkout(self):
        """
         Test if checkout is receiving Cart instance
        """
        session = self.client.session

        test_cart = self._create_testing_cart()
        self._create_testing_cart_item(
            cart_instance=test_cart,
            product_instance=self.test_product
        )
        test_cart.session_key = session.session_key
        test_cart.save()

        r = self.client.get(reverse('checkout:index'))
        r.session = session
        r.user = self.anonymous_user

        self.assertEqual(r.context['cart'], test_cart)
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'checkout_index.html')

    def test_order_string_representation(self):
        """
         Test Order model string representation
        """
        test_cart = self._create_testing_cart()
        test_user = self._create_testing_user()

        test_order = self._create_testing_order(cart=test_cart, user=test_user)
        test_order.save()

        order_str = 'Order num. {0}'.format(test_order.pk)

        self.assertEqual(str(test_order), order_str)

    def test_order_item_string_representation(self):
        """
         Test Order Item string representation
        """
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
            "Order item: {0} - {1}".format(test_order_item.id,
                test_order_item.product.name))

    def test_order_item_get_total_price(self):
        test_order_item = OrderItem(price=1000, quantity=4)
        total_price = test_order_item.get_total_price()

        self.assertEqual(total_price, 4000)
