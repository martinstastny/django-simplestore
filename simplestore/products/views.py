from django.views.generic import ListView, DetailView

from simplestore.cart.forms import AddToCartForm
from .models.product import Product, Category


class CategoryDetailView(DetailView):
    model = Category
    slug_url_kwarg = 'category_slug'
    template_name = "category_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)

        products = Product.objects.filter(
            category=self.get_object()
        ).prefetch_related('image')

        context.update({
            'products': products
        })
        return context


class ProductsListView(ListView):
    model = Product
    queryset = Product.objects.all().active().prefetch_related('image')
    template_name = "product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['form'] = AddToCartForm
        return context
