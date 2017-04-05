from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView
from .models import Order
from .forms import OrderForm
from cart.mixins import get_cart


class CheckoutView(CreateView):
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

        return super(CheckoutView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context_data = {
            'order_form': OrderForm,
            'cart': self.get_object()
        }
        context.update(context_data)
        return context
