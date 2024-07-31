import random
from django.db import models
from django.db.models import Q
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from product_inheritance.models import tag_product, size, color, brand, collect_product
from .polls import remove_spaces
from taggit.managers import TaggableManager


# Create your models here.


class productManager(models.Manager):

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_product_active(self):
        return self.get_queryset().filter(product_active=True)

    def search(self, query):
        lookup = Q(product_name__icontains=query) | Q(tags__name=query)

        return self.get_queryset().filter(lookup, product_active=True).distinct()


#
class extra_discription(models.Model):
    title_1 = models.CharField(max_length=100, verbose_name='عنوان')
    discription_1 = models.CharField(max_length=100, verbose_name='توضیحات')
    title_2 = models.CharField(max_length=100, verbose_name='عنوان')
    discription_2 = models.TextField(verbose_name='توضیحات')
    title_3 = models.CharField(max_length=100, verbose_name='عنوان')
    discription_3 = models.CharField(max_length=100, verbose_name='توضیحات')
    title_4 = models.CharField(max_length=100, verbose_name='عنوان', null=True, blank=True)
    discription_4 = models.CharField(max_length=100, verbose_name='توضیحات', null=True, blank=True)
    title_5 = models.CharField(max_length=100, verbose_name='عنوان', null=True, blank=True)
    discription_5 = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    title_6 = models.CharField(max_length=100, verbose_name='عنوان', null=True, blank=True)
    discription_6 = models.CharField(max_length=100, verbose_name='توضیحات', null=True, blank=True)
    title_7 = models.CharField(max_length=100, verbose_name='عنوان', null=True, blank=True)
    discription_7 = models.CharField(max_length=100, verbose_name='توضیحات', null=True, blank=True)
    title_8 = models.CharField(max_length=100, verbose_name='عنوان', null=True, blank=True)
    discription_8 = models.TextField(verbose_name='توضیحات', null=True, blank=True)
    title_9 = models.CharField(max_length=100, verbose_name='عنوان', null=True, blank=True)
    discription_9 = models.CharField(max_length=100, verbose_name='توضیحات', null=True, blank=True)
    title_10 = models.CharField(max_length=100, verbose_name='عنوان', null=True, blank=True)
    discription_10 = models.CharField(max_length=100, verbose_name='توضیحات', null=True, blank=True)

    class Meta:
        verbose_name = 'توضیح محصول'
        verbose_name_plural = 'توضیجات محصولات'


class Product_main_class(models.Model):
    type_choices = (('men', 'مردانه'), ('women', 'زنانه'), ('kids', 'کودکانه'))
    product_gender = models.CharField(verbose_name='جنسیت', max_length=10, choices=type_choices)
    product_name = models.CharField(max_length=80, verbose_name="نام محصول")
    product_price = models.DecimalField(max_digits=20, decimal_places=0, default=0.0, verbose_name="قیمت محصول")
    product_brand = models.ForeignKey(brand, verbose_name="برند محصول", on_delete=models.CASCADE)
    product_discription = models.TextField(max_length=200, verbose_name='توضیحات اصلی محصول')
    type_choices = (('simple', 'ساده'), ('discount', 'تخفیف'), ('new', 'جدبد'))
    product_type = models.CharField(max_length=10, choices=type_choices, default="S", verbose_name="مدل محصول")
    price_discount = models.IntegerField(default=0, verbose_name="درصد تخفیف محصول")
    product_image = models.ImageField(upload_to='upload/weblog_main/%Y/%m/%d', null=True, blank=True,
                                      verbose_name="عکس محصول")
    product_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ محصول")
    collect_products = models.ForeignKey(collect_product, verbose_name="دسته بندی", on_delete=models.CASCADE)
    product_visit = models.IntegerField(default=0, verbose_name="تعداد بازدید محصول", editable=False)
    product_active = models.BooleanField(default=False, verbose_name="فعال / غیر فعال بودن محصول")
    slug = models.SlugField(blank=True, unique=True, verbose_name="اسلاگ")
    discription = models.ForeignKey(to=extra_discription, on_delete=models.CASCADE, verbose_name='توضیحات محصول')

    tags = TaggableManager()
    objects = productManager()

    def save(self, *args, **kwargs):
        self.slug = f'{remove_spaces(self.product_name)}{random.randint(0, 999999)}مردانه'
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/product/list_view/{str(self.collect_products)}/{str(self.slug)}/{self.id}"

    def discount(self):
        if self.price_discount == 0:
            return self.product_price
        percent = float(self.price_discount / 100) * float(self.product_price)
        price = float(self.product_price) - percent
        return int(price)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'فروشگاه محصول'
        verbose_name_plural = 'فروشگاه محصولات '


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product_main_class)
