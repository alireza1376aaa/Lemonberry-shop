from django.db import models
from account_shop.models import autentication


# Create your models here.

class sitesetting(models.Model):
    address = models.TextField(verbose_name="ادرس شرکت")
    address_url = models.TextField(verbose_name="لینک ادرس در گوگل")
    email = models.EmailField(verbose_name="ایمیل شرکت")
    phone = models.CharField(max_length=90, verbose_name="تلفن شرکت")
    about_office = models.TextField(default='', verbose_name="درباره شرکت")
    logo_image = models.ImageField(upload_to="logo", null=True, blank=True, default='logo.jpg', verbose_name="عکس لوگو")
    instagrame_address = models.URLField(blank=True, null=True, verbose_name="ادرس اینستاگرام")
    telegrame_address = models.URLField(blank=True, null=True, verbose_name="ادرس تلگرام ")
    twitter_address = models.URLField(blank=True, null=True, verbose_name="ادرس تویتر")
    write_ruls = models.TextField(default='', verbose_name='قوانین کپی رایت')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'تنظیم سایت'
        verbose_name_plural = 'تنظیمات سایت'


class contact_us(models.Model):
    fullname = models.CharField(max_length=90, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل ")
    user = models.ForeignKey(autentication, on_delete=models.CASCADE, verbose_name='کاربر', null=True, blank=True)
    subject = models.CharField(max_length=90, verbose_name="موضوع")
    massege = models.TextField(verbose_name="پیغام")
    date = models.DateField(auto_now_add=True, verbose_name='تاریخ ارسال نظر', null=True, blank=True)
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده / نشده')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = 'تماس  ها'


class extra_setting(models.Model):
    privacy_text = models.TextField(verbose_name="توضیح حریم خصوصی ")
    ruls_text = models.TextField(verbose_name="توضیح شرایط و قوانین ")

    class Meta:
        verbose_name = 'تنظیم اضافه'
        verbose_name_plural = 'تنظیمات اضافه'
