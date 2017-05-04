from django.contrib import admin
from simplestore.products.models.product import Product

from simplestore.products.models.category import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)