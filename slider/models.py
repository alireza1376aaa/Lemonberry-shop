from django.db import models


# Create your models here.

class slider(models.Model):
    main_title = models.CharField(max_length=90, verbose_name="متن اصلی اسلایدر")
    about_title = models.CharField(max_length=90, verbose_name="توضیحات اسلایدر")
    seasion_title = models.CharField(max_length=90, null=True, blank=True, verbose_name="متن دلخواه برای اسلایدر")
    seasion_title_1 = models.CharField(max_length=90, null=True, blank=True, verbose_name="متن دلخواه برای اسلایدر")

    slider_image = models.ImageField(upload_to="slider", null=True, blank=True, default='defult.jpg',
                                     verbose_name="عکس اسلایدر ")

    def __str__(self):
        return self.main_title

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها '


class collection(models.Model):
    main_title = models.CharField(max_length=90, verbose_name="متن کالکشن")
    slider_image1 = models.ImageField(upload_to="slider", null=True, blank=True, default='defult.jpg',
                                      verbose_name="عکس کالکشن 1(560*380) ")
    slider_image1_responsive = models.ImageField(upload_to="slider", null=True, blank=True, default='defult.jpg',
                                                 verbose_name="عکس کالکشن ریسپانسیو 1 (171*510)")
    slider_image1_url = models.URLField(verbose_name="Url کالکشن 1 ")
    slider_image2 = models.ImageField(upload_to="slider", null=True, blank=True, default='defult.jpg',
                                      verbose_name="عکس کالکشن 2 (265*515)")
    slider_image2_responsive = models.ImageField(upload_to="slider", null=True, blank=True, default='defult.jpg',
                                                 verbose_name="عکس کالکشن ریسپانسیو 2  (171*510)")
    slider_image2_url = models.URLField(verbose_name="Url کالکشن 2 ")
    slider_image3 = models.ImageField(upload_to="slider", null=True, blank=True, default='defult.jpg',
                                      verbose_name="عکس کالکشن 3 (265*243)")
    slider_image3_responsive = models.ImageField(upload_to="slider", null=True, blank=True, default='defult.jpg',
                                                 verbose_name="عکس کالکشن ریسپانسیو 3 (171*510)")
    slider_image3_url = models.URLField(verbose_name="Url کالکشن 3 ")
    slider_image4 = models.ImageField(upload_to="slider", null=True, blank=True, default='defult.jpg',
                                      verbose_name="عکس کالکشن 4 (265*790)")
    slider_image4_responsive = models.ImageField(upload_to="slider", null=True, blank=True, default='defult.jpg',
                                                 verbose_name="عکس کالکشن ریسپانسیو 4 (171*510)")
    slider_image4_url = models.URLField(verbose_name="Url کالکشن 4 ")

    def __str__(self):
        return self.main_title

    class Meta:
        verbose_name = 'کالکشن'
        verbose_name_plural = 'کالکشن ها '
