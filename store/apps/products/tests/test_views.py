from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse, resolve
from products.models.product import Product
from products.views import ProductsListView, ProductDetailView

class ProductViewsTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.product_list_url = reverse('products:index')
        self.product_detail_url = reverse('products:detail', kwargs={'slug': self.product_first.slug})

    @classmethod
    def setUpTestData(cls):
        """
        Create 3 product objects which one of them is not active
        """
        cls.product_first = Product.objects.create(
            name='Test Product',
            price=100,
            slug='test-product',
            sku='PROD001',
            is_active=True,
        )

        cls.product_seconds = Product.objects.create(
            name='Test Product 2',
            slug='test-product-2',
            price=150,
            sku='PROD002',
            is_active=True,
        )

        cls.product_third = Product.objects.create(
            name='Test Product 3',
            slug='test-product-3',
            price=160,
            sku='PROD200001',
            is_active=False,
        )

    # Products Category tests

    """Check if ProductList URL is matching correct view."""
    def test_products_list_resolves_to_product_list_view(self):
        product_list = resolve(self.product_list_url)
        self.assertEqual(product_list.func.__name__, ProductsListView.__name__)

    """
    Check if ProductList URL is using correct template.
    """
    def test_products_list_use_product_list_template(self):
        url = self.client.get(self.product_list_url)
        self.assertTemplateUsed(url, template_name='product_list.html')

    """
    ProductListView should return success response
    """
    def test_products_to_return_success_response(self):
        request = self.factory.get(self.product_list_url)
        response = ProductsListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    """
    Check if View is returning queryset for active products
    data: setUpTestData method
    """
    def test_products_list_view_is_returning_active_products(self):
        request = self.client.get(self.product_list_url)
        self.assertEqual(len(request.context_data['object_list']), 3)


    # Product Detail tests
    """
    Check if Product Detail URL is matching the correct view.
    """
    def test_product_detail_url_resolves_to_product_detail_view(self):
        product_detail = resolve(self.product_detail_url)
        self.assertEqual(product_detail.func.__name__, ProductDetailView.__name__)

    def test_if_product_detail_object_returns_correct_status_code_and_product_name(self):
        response = self.client.get(self.product_first.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['object']), self.product_first.name)