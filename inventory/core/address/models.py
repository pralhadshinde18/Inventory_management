from django.db import models
from core.models.abstract import TimeStampAbstractModel
from enum import Enum


class AddressType(Enum):
    BILLING = 'billing_address'
    SHIPPING = 'shipping_address'


class Address(TimeStampAbstractModel):
    address_id = models.IntegerField()
    customer_id = models.IntegerField()
    address_type = models.CharField(max_length=50,
                                    choices=[(choice.value,choice.name) for choice in AddressType],
                                    default= AddressType.BILLING.value
                                    )
    house_no = models.IntegerField()
    lane = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.IntegerField()

    class meta:
        verbose_name_plural = "addresses"

    def __str__(self):
        return str(self.address_id)
