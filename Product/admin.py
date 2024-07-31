from django.contrib import admin
from .models import Product_main_class,extra_discription


# Register your models here.

class filter_pro(admin.ModelAdmin):
    list_display = ['__str__','collect_products','product_type']
    list_filter = ['product_active']
    search_fields = ['product_name']

    class meta:
        model = Product_main_class


admin.site.register(Product_main_class, filter_pro)
admin.site.register(extra_discription)
