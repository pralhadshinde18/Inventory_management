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
from core.product.api import product_details, product_list, create_product,update_product,delete_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', product_list),
    path('product/<int:product_id>/', product_details),
    path('product-create/', create_product),
    path('product-update/<int:product_id>/', update_product),
    path('product-delete/<int:product_id>/', delete_product),

]
