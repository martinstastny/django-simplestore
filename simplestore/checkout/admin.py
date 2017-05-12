from django.contrib import admin
from .models.order import Order, OrderItem
from .models.address import Address
from .models.delivery import Delivery
from .models.payment import Payment


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = False
    readonly_fields = ('product', 'price', 'total_price', 'quantity',)


class AddressAdmin(admin.ModelAdmin):
    model = Address


class DeliveryAdmin(admin.ModelAdmin):
    model = Delivery


class PaymentAdmin(admin.ModelAdmin):
    model = Payment


class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ('cart', 'full_name', 'email', 'shipping_address', 'billing_address', 'payment_method', 'phone', 'delivery_method',)
    inlines = [
        OrderItemInline,
    ]


admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Payment, PaymentAdmin)
