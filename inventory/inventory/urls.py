"""
URL configuration for inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.customer.api import customer_list, customer_details, create_customer,update_customer,delete_customer
from core.address.api import address_list,address_details,create_address,update_address,delete_address
from core.product.api import product_list, product_details, create_product,update_product,delete_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', customer_list),
    path('address/<int:customer_id>/', customer_details),
    path('create_customer/', create_customer),
    path('update_customer/<int:customer_id>/', update_customer),
    path('delete_customer/<int:customer_id>/', delete_customer),

    path('address/', address_list),
    path('address/<int:address_id>/', address_details),
    path('create_address/',create_address),
    path('update_address/<int:address_id>/',update_address),
    path('delete_address/<int:address_id>/',delete_address),

    path('product/', product_list),
    path('product/<int:product_id>/', product_details),
    path('create_product/',create_product),
    path('update_product/<int:product_id>/',update_product),
    path('delete_product/<int:product_id>/',delete_product),

]
