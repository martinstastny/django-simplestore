from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView
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
        order = form.save(commit=False)
        order.cart = self.get_object()
        order.save()

        order.create_order_items()

        self.request.session.create()

        return redirect(order.get_absolute_url())

    def get_context_data(self, **kwargs):
        context_data = super(CheckoutOrderCreateView, self).get_context_data(**kwargs)
        context_data['cart'] = self.get_object()
        return context_data


class OrderConfirmationView(DetailView):
    model = Order
    template_name = "order_confirmation.html"

    def get_context_data(self, **kwargs):
        context_data = super(OrderConfirmationView, self).get_context_data()
        return context_data
