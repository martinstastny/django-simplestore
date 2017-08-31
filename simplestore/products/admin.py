from django.contrib import admin

from simplestore.products.models.category import Category
from simplestore.products.models.product import Product


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('name', 'sku', 'price', 'slug', 'is_active',)
    ordering = ['-is_active', 'name']
    list_filter = ('is_active',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
