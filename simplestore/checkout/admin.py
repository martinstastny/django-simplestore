from django.contrib import admin

from .models.address import Address
from .models.delivery import Delivery
from .models.order import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = False
    readonly_fields = ('product', 'price', 'total_price', 'quantity',)


class AddressAdmin(admin.ModelAdmin):
    model = Address


class DeliveryAdmin(admin.ModelAdmin):
    model = Delivery


class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = (
        'cart',
        'full_name',
        'user',
        'email',
        'shipping_address',
        'phone',
        'delivery_method',
    )
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Delivery, DeliveryAdmin)
