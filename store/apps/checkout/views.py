from django.shortcuts import redirect
from django.views.generic import CreateView
from .models import Order
from .forms import OrderForm
from cart.mixins import get_cart


class CheckoutOrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "checkout_index.html"

    def get_object(self, queryset=None):
        cart = get_cart(self.request)
        return cart

    def get(self, request, *args, **kwargs):
        cart = self.get_object()

        if cart.cartitem_set.exists() is False:
            return redirect('cart:index')

        return super(CheckoutOrderCreateView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        pass

    def get_context_data(self, **kwargs):
        context_data = super(CheckoutOrderCreateView, self).get_context_data(**kwargs)
        context_data['cart'] = self.get_object()
        return context_data