from django.shortcuts import redirect
from django.views.generic import DetailView, FormView
from cart.mixins import get_cart
from .models.order import Order
from .forms import OrderForm, AddressForm, DeliveryForm, PaymentForm


class CheckoutOrderCreateView(FormView):
    model = Order
    template_name = "checkout_index.html"

    def get_object(self):
        cart = get_cart(self.request)
        return cart

    def get(self, request, *args, **kwargs):
        cart = self.get_object()
        order_form = OrderForm()
        address_form = AddressForm()
        delivery_form = DeliveryForm()
        payment_form = PaymentForm()

        if cart.cartitem_set.exists() is False:
            return redirect('cart:index')

        return self.render_to_response(context={
            'cart': cart,
            'order_form': order_form,
            'address_form': address_form,
            'delivery_form': delivery_form,
            'payment_form': payment_form
        })

    def post(self, request, *args, **kwargs):
        order_form = OrderForm(request.POST)
        address_form = AddressForm(request.POST)
        delivery_form = DeliveryForm(request.POST)
        payment_form = PaymentForm(request.POST)

        if order_form.is_valid() and address_form.is_valid() and delivery_form.is_valid() and payment_form.is_valid():
            return self.process_order(order_form, address_form, delivery_form, payment_form, **kwargs)
        else:
            return self.render_to_response(context={
                'cart': self.get_object(),
                'order_form': order_form,
                'address_form': address_form,
                'delivery_form': delivery_form,
                'payment_form': payment_form
             })

    def process_order(self, order_form, address_form, delivery_form, payment_form, **kwargs):
        address = address_form.save(commit=False)
        order = order_form.save(commit=False)

        if address.use_as_billing:
            address.address_type = 'shipping'
        else:
            address.address_type = 'billing'

        address.save()

        order.cart = self.get_object()
        order.shipping_address = address
        order.payment_method = payment_form.cleaned_data['payment_method']
        order.delivery_method = delivery_form.cleaned_data['delivery_method']

        if self.request.user.is_authenticated():
            order.user = self.request.user

        order.save()
        order.create_order_items()

        try:
            del self.request.session['user_cart']
        except KeyError:
            self.request.session.create()

        return redirect(order.get_absolute_url())


class OrderConfirmationView(DetailView):
    model = Order
    template_name = "order_confirmation.html"

    def get_context_data(self, **kwargs):
        context_data = super(OrderConfirmationView, self).get_context_data()
        return context_data