from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView, View, TemplateView
from .models.order import Order, Address
from .forms import OrderForm, AddressForm
from cart.mixins import get_cart


class CheckoutOrderCreateView(FormView):
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

    def post(self, request, *args, **kwargs):
        order_form = OrderForm(request.POST)
        address_form = AddressForm(request.POST)

        if order_form.is_valid() and address_form.is_valid():
            return self.form_valid(order_form, address_form)
        else:
            self.form_invalid(order_form, address_form)

    def form_invalid(self, order_form, address_form):
        print('not valid')


    def form_valid(self, order_form, address_form):
        address = address_form.save(commit=False)
        order = order_form.save(commit=False)

        if address.use_as_billing:
            address.address_type = 'shipping'
        else:
            address.address_type = 'billing'

        address.save()

        order.cart = self.get_object()
        order.shipping_address = address

        if self.request.user.is_authenticated():
            order.user = self.request.user

        order.save()
        order.create_order_items()

        try:
            del self.request.session['user_cart']
        except KeyError:
            self.request.session.create()

        # return super(CheckoutOrderCreateView, self).form_valid(self)
        return redirect(order.get_absolute_url())


    def get_context_data(self, **kwargs):
        context_data = super(CheckoutOrderCreateView, self).get_context_data(**kwargs)
        context_data['order_form'] = OrderForm()
        context_data['address_form'] = AddressForm()
        context_data['cart'] = self.get_object()
        return context_data


class OrderConfirmationView(DetailView):
    model = Order
    template_name = "order_confirmation.html"

    def get_context_data(self, **kwargs):
        context_data = super(OrderConfirmationView, self).get_context_data()
        return context_data
