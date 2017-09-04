from django import forms

from .models.address import Address
from .models.order import Order


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'postcode', 'country']


class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone']
