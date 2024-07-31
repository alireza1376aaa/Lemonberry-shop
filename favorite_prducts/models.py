from django.db import models
from account_shop.models import autentication
from Product.models import Product_main_class
from datetime import datetime


# Create your models here.

class manager(models.Manager):

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(product_id=product_id)

        return qs.first()


class favorite(models.Model):
    owner = models.ForeignKey(autentication, on_delete=models.CASCADE, verbose_name="id کاربر")
    product_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ")
    product = models.ForeignKey(Product_main_class, on_delete=models.CASCADE)
    objects = manager()

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'محصول مورد علاقه'
        verbose_name_plural = 'محصولات مورد علاقه'
