from django.db import models
from core.models.abstract import TimeStampAbstractModel


class Product(TimeStampAbstractModel):
    product_name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = "product"

    def __str__(self):
        return self.product_name
