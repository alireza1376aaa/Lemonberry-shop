from django.db import models
from shopping_cart.models import Final_cart


# Create your models here.
class Send_Factor(models.Model):
    basket = models.ForeignKey(Final_cart, on_delete=models.PROTECT, verbose_name="سبد خرید")
    send = models.BooleanField(default=False, verbose_name="ارسال شده / نشده")
    factor = models.FileField(upload_to='product_shop/factor', null=True, blank=True, verbose_name="سند خرید pdf")

    class Meta:
        verbose_name = 'ارسال کردن محصول'
        verbose_name_plural = 'ارسال کردن محصولات'
