from django import forms
from .models import CartItem


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = [
            'quantity'
        ]
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'full-width'})
        }
