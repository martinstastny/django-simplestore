from django import forms
from .models import Order, Address
from django.conf import settings

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'street',
            'city',
            'state',
            'zip_code',
            # 'address_type'
        ]
        # widgets = {
        #     'address_type': forms.RadioSelect(choices=settings.ADDRESS_TYPE)
        # }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name',
            'last_name',
            'email',
            'email2',
            'phone',
        ]