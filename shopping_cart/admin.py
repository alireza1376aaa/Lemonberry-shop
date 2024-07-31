from django.contrib import admin
from shopping_cart.models import Final_cart, finally_order, Cart


# Register your models here.
@admin.register(Final_cart)
class OrderAdmin_Final(admin.ModelAdmin):
    list_display = ["user_id", 'is_pay']

    def change_view(self, request, object_id, form_url="", extra_context=None):
        if not request.user.is_superuser:
            self.exclude = ('company',)
        extra_context = extra_context or {}
        return super().change_view(request, object_id, form_url, extra_context=extra_context, )


@admin.register(Cart)
class OrderAdmin_Cart(admin.ModelAdmin):
    list_display = ["final_cart", 'product_id', 'color_size']


admin.site.register(finally_order)
