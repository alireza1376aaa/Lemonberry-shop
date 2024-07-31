from django.db import models
from django.utils.crypto import get_random_string
from Product.models import Product_main_class
from account_shop.models import autentication
from Product_details.models import Count


# Create your models here.

class Final_cart(models.Model):
    user_id = models.ForeignKey(autentication, on_delete=models.CASCADE, related_name='user_cart',
                                verbose_name="نام کاربری")
    is_pay = models.BooleanField(default=False, null=True, blank=True, verbose_name='پرداخت شده / نشده')
    date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')
    code_tr = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name='کد تایید')
    Order_number = models.CharField(max_length=12, null=True, unique=True, blank=True, verbose_name='شماره سفارش')

    def __str__(self):
        return self.user_id.email

    def save(self, *args, **kwargs):
        if self.Order_number is None:
            self.Order_number = f'{get_random_string(4)}-{get_random_string(4)}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'نهایی کردن سبد خرید'
        verbose_name_plural = 'نهایی کردن سبدهای خرید'

    def total_price(self):
        total_pri = 0
        if self.is_pay:
            for cart in self.cart_set.all():
                total_pri += cart.old_total_price()
        else:
            for cart in self.cart_set.all():
                if cart.product_id.product_type == 'discount':
                    total_pri += cart.product_id.discount() * cart.count
                else:
                    total_pri += cart.product_id.product_price * cart.count
        return total_pri

    def total_price_with_delivery(self):
        total_pri = self.total_price()
        if total_pri < 500000:
            return total_pri + 30000
        else:
            return total_pri

    def total_price_without_discount(self):
        total_pri = 0
        if self.is_pay:
            for cart in self.cart_set.all():
                total_pri += cart.old_total_price_without_discount()
            return total_pri
        else:
            return total_pri


class manager(models.Manager):

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(product_id=product_id)

        return qs.first()


class Cart(models.Model):
    final_cart = models.ForeignKey(Final_cart, on_delete=models.CASCADE, verbose_name='سبدخرید')
    product_id = models.ForeignKey(Product_main_class, on_delete=models.CASCADE, verbose_name="محصول")
    count = models.IntegerField(verbose_name='تعداد')
    color_size = models.ForeignKey(to=Count, on_delete=models.CASCADE, verbose_name='رنگ , سایز')
    final_price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True,
                                      verbose_name='قیمت نهایی تکی محصول')
    final_price_discount = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True,
                                               verbose_name='درصد تخفیف نهایی تکی محصول', default=0)
    objects = manager()

    def __str__(self):
        return self.product_id.product_name

    def total_price(self):
        if self.product_id.product_type == 'discount':
            return int(self.count * self.product_id.discount())

        else:
            return int(self.count * self.product_id.product_price)

    def old_total_price(self):
        if self.final_price_discount > 0:
            dic = int(float(self.final_price) - (float(self.final_price_discount / 100) * float(self.final_price)))
            total = int(self.count * dic)
        else:
            total = int(self.count * self.final_price)
        return total

    def old_total_price_without_discount(self):
        total = int(self.count * self.final_price)
        return int(total)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = ' سبدهای خرید'


class finally_order(models.Model):
    user = models.ForeignKey(to=autentication, on_delete=models.CASCADE)
    phone = models.TextField(verbose_name="شماره")
    fullname = models.TextField(verbose_name="نام کامل ")
    address = models.TextField(verbose_name="ادرس ")
    post_code = models.CharField(max_length=90, verbose_name="کد پستی")
    city = models.CharField(max_length=90, verbose_name="شهر")
    city_location = models.CharField(max_length=90, verbose_name="استان")
    factor_code = models.CharField(max_length=90, verbose_name="کد سفارش")

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'ادرس ارسال کردن'
        verbose_name_plural = 'ادرس های ارسال کردن'
