from django.contrib import admin
from core.customer.models import Customer
from core.address.models import Address
from core.category.models import Category
from core.product.models import Product


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')
    list_filter = ('full_name',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('customer_id','address_type')
    list_filter = ('customer_id',)

@admin.register(Category)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('category_id','category_name')
    list_filter = ('category_id',)

@admin.register(Product)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('product_name','description')
    list_filter = ('product_name',)

