from django.contrib import admin
from products.models.product import Product
from products.models.category import Category

# class ProductSizeVariantAdmin(admin.TabularInline):
#     model = SizeVariant


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    # inlines = [
    #     ProductSizeVariantAdmin
    # ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)