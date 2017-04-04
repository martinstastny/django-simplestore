from django.contrib import admin
from .models import Order, Address

class AddressAdmin(admin.ModelAdmin):
    pass

class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)