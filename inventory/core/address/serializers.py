from rest_framework import serializers
from core.address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id','address_id','customer_id','address_type','house_no','lane','city','state','country','pincode',]


class AddressDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id']
