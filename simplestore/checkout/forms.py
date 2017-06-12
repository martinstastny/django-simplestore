from django import forms

from .models.order import Order
from .models.address import Address
from .models.delivery import Delivery
from .models.payment import Payment


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'street',
            'city',
            'postcode',
            'country',
            # 'use_as_billing'
        ]


class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'full_name',
            'email',
            'phone',
        ]


class DeliveryMethodForm(forms.Form):
    delivery_method = forms.ModelChoiceField(queryset=Delivery.objects.all(), widget=forms.RadioSelect,
                                             empty_label=None, initial=None, required=True, label='')

class PaymentForm(forms.Form):
    number = forms.IntegerField()
    expire_date = forms.CharField()
    ccv = forms.IntegerField()