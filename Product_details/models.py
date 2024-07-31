from django.db import models
from Product.models import Product_main_class
from product_inheritance.models import size, color
from account_shop.models import autentication


# Create your models here.


class Count(models.Model):
    product_size = models.ForeignKey(to=size, on_delete=models.CASCADE, verbose_name='سایز انتخابی')
    product_color = models.ForeignKey(to=color, on_delete=models.CASCADE, verbose_name='رنگ انخابی انتخابی')
    count_pro = models.IntegerField(verbose_name='تعداد موجودی', )

    Product_main_class = models.ForeignKey(to=Product_main_class, on_delete=models.CASCADE, null=True, blank=True)

    # product_women = models.ForeignKey(to=Product_main_class,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_size}+{self.product_color}'


class product_gallery(models.Model):
    title = models.CharField(max_length=80, verbose_name="عنوان محصول", blank=True)
    image = models.ImageField(upload_to="product_shop/product_gallery", null=True, blank=True, default='defult.jpg',
                              verbose_name="عکس های محصول")

    Product_main_class = models.ForeignKey(Product_main_class, on_delete=models.CASCADE, null=True, blank=True)

    # product_women = models.ForeignKey(Product_main_class, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        title = ''
        if self.Product_main_class is not None:
            title = self.Product_main_class.product_name
        self.title = title
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'گالری عکس'
        verbose_name_plural = 'گالری عکس ها'


class comment(models.Model):
    parent = models.ForeignKey('comment', null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(to=autentication, on_delete=models.CASCADE, verbose_name='کاربر')
    product_id = models.ForeignKey(Product_main_class, on_delete=models.CASCADE)
    subject = models.CharField(max_length=90, verbose_name="موضوع")
    massege = models.TextField(verbose_name="پیغام")
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده / نشده')
    data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = 'کامنت ها'
