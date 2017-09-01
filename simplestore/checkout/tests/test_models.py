import datetime

from django.test import TestCase

from simplestore.cart.models import Cart, CartItem
from simplestore.checkout.models.order import Order
from simplestore.products.models.product import Product
from simplestore.profiles.models import Profile


class TestOrderModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Testing Product
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

        # Testing cart
        cls.cart = Cart(
            created=datetime.datetime.now(),
            updated=datetime.datetime.now()
        )
        cls.cart.save()

        # Testing Cart Items
        cls.cart_item = CartItem(
            cart=cls.cart,
            product=cls.test_product,
            quantity=1,
            date_added=datetime.datetime.now()
        )
        cls.cart_item.save()

        # Testing Profile
        cls.test_user = Profile()

    def test_order_detail_get_absolute_url(self):
        order = Order(
            cart=self.cart,
            full_name='Martin Stastny',
            email='testmail@gmail.com',
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )

        order.save()

        response = self.client.get(order.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_add_order_items_to_order(self):
        order = Order(
            cart=self.cart,
            full_name='Martin Stastny',
            email='testmail@gmail.com',
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )

        order.save()
        order.create_order_items()

        self.assertEqual(order.items.count(), 1)
        self.assertEqual(str(order), 'Order num. 1')
