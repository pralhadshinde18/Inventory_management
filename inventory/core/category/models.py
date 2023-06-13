from django.db import models
from core.models.abstract import TimeStampAbstractModel


class Category(TimeStampAbstractModel):
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name


class SubCategory(TimeStampAbstractModel):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='subcategories')
    subcategory_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "subcategories"

    def __str__(self):
        return self.subcategory_name
