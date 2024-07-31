from django.contrib import admin
from .models import size, brand, color, collect_product, tag_product


class filterxx(admin.ModelAdmin):
    list_display = ['product_brand', 'women', 'men']
    list_filter = ['women', 'men']

    class meta:
        model = brand


class filter(admin.ModelAdmin):
    list_display = ['title_collect_product_main','name_collect_product_main','parent','gender']
    list_filter = ['gender']
    class meta:
        model = collect_product


# Register your models here.
admin.site.register(size)
admin.site.register(brand,filterxx)
admin.site.register(color)
admin.site.register(collect_product, filter)
