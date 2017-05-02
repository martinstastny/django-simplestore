from django.contrib import admin
from .models import Cart, CartItem
#
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    exclude = ('product',)
    readonly_fields = ('quantity',)

class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('id', 'user', 'created', 'updated',)
    inlines = [
        CartItemInline
    ]

admin.site.register(Cart, CartAdmin)