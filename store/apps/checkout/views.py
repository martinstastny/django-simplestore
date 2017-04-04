from django.views.generic import CreateView
from .models import Order
from .forms import AddressForm, OrderForm
from cart.mixins import get_cart

class CheckoutView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "checkout_index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CheckoutView, self).get_context_data(*args, **kwargs)
        context_data = {
            'address_form': AddressForm,
            'order_form': OrderForm,
            'cart': get_cart(self.request)
        }
        context.update(context_data)
        return context
