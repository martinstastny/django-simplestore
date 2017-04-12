from .models.product import Product
from django.views.generic import ListView, DetailView
from cart.forms import AddToCartForm

class ProductsListView(ListView):
    model = Product
    queryset = Product.objects.prefetch_related('image')
    template_name = "product_list.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['form'] = AddToCartForm
        return context