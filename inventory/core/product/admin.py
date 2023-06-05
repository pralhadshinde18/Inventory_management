from django.contrib import admin
from core.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name',)
    list_filter = ('product_name',)
