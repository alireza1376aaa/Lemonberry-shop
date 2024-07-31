from django.contrib import admin
from .models import Count, product_gallery, comment


class filter(admin.ModelAdmin):
    list_display = ['__str__', 'Product_main_class']


# Register your models here.
admin.site.register(Count, filter)
admin.site.register(product_gallery)
admin.site.register(comment)
