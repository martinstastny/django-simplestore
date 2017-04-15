from django.contrib import admin
from .models.order import Order, OrderItem
from .models.address import Address
from .models.delivery import Delivery
from .models.payment import Payment

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class AddressAdmin(admin.ModelAdmin):
    model = Address

class DeliveryAdmin(admin.ModelAdmin):
    model = Delivery

class PaymentAdmin(admin.ModelAdmin):
    model = Payment

class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ('full_name', 'email', 'shipping_address', 'billing_address', )
    inlines = [
        OrderItemInline,
    ]

admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Payment, PaymentAdmin)