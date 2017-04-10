from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderItemInline
    ]

admin.site.register(Order, OrderAdmin)