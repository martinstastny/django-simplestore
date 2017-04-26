from django import forms
from .models.order import Order
from .models.address import Address
from .models.delivery import Delivery
from .models.payment import Payment


class ShippingAddressForm(forms.ModelForm):
    prefix = 'shipping_address'
    class Meta:
        model = Address
        fields = [
            'street',
            'city',
            'postcode',
            'country',
            'use_as_billing'
        ]


class BillingAddressForm(forms.ModelForm):
    prefix = 'billing_address'
    class Meta:
        model = Address
        fields = '__all__'
        exclude = [
            'use_as_billing',
            'address_type'
        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'full_name',
            'email',
            'phone',
        ]


class DeliveryForm(forms.Form):
    delivery_method = forms.ModelChoiceField(queryset=Delivery.objects.all(), widget=forms.RadioSelect,
                                             empty_label=None, initial=None, required=True, label='')


class PaymentForm(forms.Form):
    payment_method = forms.ModelChoiceField(
        queryset=Payment.objects.all(), widget=forms.RadioSelect, empty_label=None,
                                            initial=None, label='')
