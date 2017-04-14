from django import forms
from django.forms.models import inlineformset_factory, modelformset_factory
from .models.order import Order
from .models.address import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'street',
            'city',
            'postcode',
            'country',
            'use_as_billing'
        ]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'full_name',
            'email',
            'phone',
        ]

