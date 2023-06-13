from django.db import models
from core.models.abstract import TimeStampAbstractModel


class Customer(TimeStampAbstractModel):
    customer_id = models.IntegerField()
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_no = models.IntegerField()

    class meta:
        verbose_name_plural = "customers"

    def __str__(self):
        return str(self.customer_id)

