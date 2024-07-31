from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
import random
from Product.polls import remove_spaces


# Create your models here.


class size(models.Model):
    product_size = models.CharField(max_length=50, verbose_name="سایز محصول")
    product_unit = models.CharField(max_length=50, verbose_name="واحد سایز")

    def __str__(self):
        return self.product_size

    class Meta:
        verbose_name = 'سایز محصول'
        verbose_name_plural = 'سایز محصولات'


class color(models.Model):
    product_color = models.CharField(max_length=50, verbose_name="رنگ محصول")
    product_color_english = models.CharField(max_length=50, verbose_name="رنگ محصول به انگلیسی", null=True, blank=True)

    def __str__(self):
        return self.product_color

    class Meta:
        verbose_name = 'رنگ محصول'
        verbose_name_plural = 'رنگ محصولات'


class brand(models.Model):
    product_brand = models.CharField(max_length=50, verbose_name="برند محصول")
    women = models.BooleanField(default=False, verbose_name='برند زنانه')
    men = models.BooleanField(default=False, verbose_name='برند مردانه')

    def __str__(self):
        return self.product_brand

    class Meta:
        verbose_name = 'برند محصول'
        verbose_name_plural = 'برند محصولات'


class collect_product(models.Model):
    parent = models.ForeignKey('collect_product', on_delete=models.CASCADE, verbose_name='خانواده دسته بندی',
                               null=True, blank=True, )
    title_collect_product_main = models.CharField(max_length=80, verbose_name="عنوان دسته بندی", blank=True)
    type_choices = (('men', 'مردانه'), ('women', 'زنانه'), ('kids', 'کودکانه'))
    gender = models.CharField(null=True, blank=True, verbose_name='جنسیت', max_length=10, choices=type_choices)
    name_collect_product_main = models.CharField(max_length=80, verbose_name="نام دسته بندی در url", blank=True)

    def __str__(self):
        return self.title_collect_product_main

    class Meta:
        verbose_name = 'دسته بندی '
        verbose_name_plural = 'دسته بندی  محصولات'

    def save(self, *args, **kwargs):
        self.name_collect_product_main = f'{remove_spaces(self.title_collect_product_main)}{random.randint(1, 100)}'
        return super().save(*args, **kwargs)


class tag_productManager(models.Manager):

    def get_product_active(self):
        return self.get_queryset().filter(product_active=True)


class tag_product(models.Model):
    product_title = models.CharField(max_length=20, verbose_name="نام تگ")
    product_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ تگ")
    product_active = models.BooleanField(default=False, verbose_name="فعال / غیر فعال بودن تگ")
    slug = models.SlugField(blank=True, unique=True, verbose_name="اسلاگ")
    objects = tag_productManager()

    def __str__(self):
        return self.product_title

    class Meta:
        verbose_name = 'مدل تگ'
        verbose_name_plural = 'مدل های تگ'


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=tag_product)
