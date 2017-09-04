import datetime
from decimal import Decimal

from django.contrib.auth.models import AnonymousUser
from django.contrib.messages import get_messages
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from simplestore.cart.models import Cart, CartItem
from simplestore.cart.templatetags.cart_tags import cart_counter
from simplestore.cart.utils import get_cart
from simplestore.products.models.product import Product
from simplestore.profiles.models import Profile


class CartViewsTests(TestCase):
    def setUp(self):
        self.request = RequestFactory()
        self.request.session = {}
        self.request.anonymous_user = AnonymousUser()

    @classmethod
    def setUpTestData(cls):
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

    def _create_testing_cart(self, *args, **kwargs):
        cart = Cart(
            created=datetime.datetime.now(),
            updated=datetime.datetime.now(),
            *args,
            **kwargs
        )
        cart.save()

        return cart

    def _create_testing_cart_item(self, cart_instance, product_instance):
        cart_item = CartItem(
            cart=cart_instance,
            product=product_instance,
            quantity=1,
            date_added=datetime.datetime.now()
        )
        cart_item.save()

        return cart_item

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

    def test_cart_string_representation(self):
        cart = self._create_testing_cart()
        self.assertEqual(str(cart), 'Cart id: {id}'.format(id=cart.pk))

    def test_empty_cart_view(self):
        response = self.client.get(reverse('cart:index'))
        self.assertEqual(response.status_code, 200)

    def test_resolve_cart_for_logged_in_user(self):
        session = self.client.session
        session['user_cart'] = 'testing_session'

        request = self.client.get(reverse('cart:index'))
        request.user = self._create_testing_user()
        request.session = session

        testing_cart = self._create_testing_cart()
        testing_cart.session_key = request.session['user_cart']
        testing_cart.user = request.user
        testing_cart.save()

        cart = get_cart(request)

        self.assertEqual(request.status_code, 200)
        self.assertEqual(cart, testing_cart)

    def test_resolve_cart_for_anonymous_user(self):
        session = self.client.session

        testing_cart = self._create_testing_cart()
        testing_cart.session_key = session.session_key
        testing_cart.save()

        request = self.client.get(reverse('cart:index'))
        request.session = session
        request.user = AnonymousUser()

        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.context['cart'], testing_cart)

    def test_string_representation_cart_item(self):
        cart = self._create_testing_cart()
        cart_item = self._create_testing_cart_item(
            cart_instance=cart,
            product_instance=self.test_product
        )

        self.assertEqual(str(cart_item), cart_item.product.name)

    def test_cart_item_url(self):
        cart = self._create_testing_cart()
        cart_item = self._create_testing_cart_item(
            cart_instance=cart,
            product_instance=self.test_product
        )
        response = self.client.get(cart_item.get_absolute_url())
        self.assertTrue(response.status_code, 200)

    def test_deleting_cart_item(self):
        session = self.client.session

        cart = self._create_testing_cart()
        cart.session_key = session.session_key
        cart.save()

        cart_item = self._create_testing_cart_item(
            cart_instance=cart,
            product_instance=self.test_product
        )

        response = self.client.post(reverse('cart:remove',
            kwargs={'product_id': cart_item.product_id}),
            data={'product_id': cart_item.product_id}, follow=True)

        messages = [msg for msg in get_messages(response.wsgi_request)]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(messages[0].tags,
            'success',
            'Message type should return success type'
        )
        self.assertEqual(
            messages[0].message,
            'The item has been deleted from your cart.',
            'Message text should be equal to: The item has been deleted from '
            'your cart')
        self.assertEqual(cart.items.count(), 0, 'Cart should have zero items.')

    def test_updating_cart_item(self):
        session = self.client.session

        cart = self._create_testing_cart()
        cart.session_key = session.session_key
        cart.save()

        cart_item = self._create_testing_cart_item(cart_instance=cart, product_instance=self.test_product)

        response = self.client.post(reverse('cart:update', kwargs={'pk': cart_item.pk}),
            data={'cart_item_quantity': '2'}, follow=True
        )

        messages = [msg for msg in get_messages(response.wsgi_request)]

        updated_quantity = response.context['cart'].items.first().quantity
        cart_item.quantity = updated_quantity
        cart_item.save()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(cart_item.quantity, 2)
        self.assertEqual(cart_item.total_price, Decimal(cart_item.quantity * cart_item.product.price))
        self.assertEqual(messages[0].tags, 'success', 'Message type should return success type')
        self.assertEqual(messages[0].message, 'Product quantity has been updated.')

    def test_amending_quantity_on_existing_item(self):
        session = self.client.session

        request = self.client.post(reverse('cart:add', kwargs={'product_id': self.test_product.id}),
            data={'quantity': 1}, follow=True)
        request.session = session
        request.user = AnonymousUser()

        quantity = 1

        cart = get_cart(request)
        cart_item, cart_item_created = CartItem.objects.update_or_create(
            cart=cart, product=self.test_product)

        if cart_item_created == False:
            cart_item.quantity += quantity

        cart_item.save()

        self.assertEqual(cart_item.quantity, 2)

    def test_adding_item_to_cart_as_anonymous_user(self):
        response = self.client.post(
            reverse('cart:add', kwargs={'product_id': self.test_product.id}),
            data={'quantity': 2}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['cart'].items.first().quantity, 2,
            'Quantity should be equal to 2')
        self.assertEqual(response.context['cart'].items.count(), 1)

    def test_adding_item_to_cart_as_logged_user(self):
        session = self.client.session
        session['user_cart'] = 'cart_session'

        test_user = self._create_testing_user()

        response = self.client.post(
            reverse('cart:add', kwargs={'product_id': self.test_product.id}),
            data={'quantity': 3}, follow=True)

        response.session = session
        response.user = test_user

        cart, created = Cart.objects.get_or_create(
            session_key=response.session['user_cart'], user=response.user)
        cart.save()

        self.assertRedirects(response, '/cart/', 302)
        self.assertEqual(response.context['cart'].items.count(), 1)
        self.assertEqual(response.context['cart'].items.first().quantity, 3)

    def test_get_total_quantity_of_items_in_cart(self):
        session = self.client.session
        session['user_cart'] = 'cart_session'

        cart = self._create_testing_cart()

        # Products
        product = self.test_product
        product_2 = self.test_product

        cart_item = self._create_testing_cart_item(cart_instance=cart,
            product_instance=product)
        cart_item.quantity = 3
        cart_item.save()

        cart_item_2 = self._create_testing_cart_item(cart_instance=cart,
            product_instance=product_2)
        cart_item_2.quantity = 2
        cart_item_2.save()

        cart.save()

        total_qty_of_items = cart.get_total_quantity_of_items()

        self.assertEqual(total_qty_of_items, 5, "It should return 5")

    def test_context_processors(self):
        session = self.client.session

        cart = self._create_testing_cart()
        cart_item = self._create_testing_cart_item(
            cart_instance=cart,
            product_instance=self.test_product
        )
        cart_item.quantity = 3
        cart_item.save()

        cart.session_key = session.session_key
        cart.save()

        request = self.client.get(reverse('cart:index'))
        request.session = session
        request.user = self.request.anonymous_user

        context = {
            'request': request
        }

        total_qty = cart_counter(context)

        self.assertEqual(total_qty['cart_items_total_qty'], 3,
            "Total quantity should be equal to 3"
        )
