from django.contrib import admin
from .models import Send_Factor


# Register your models here.

@admin.register(Send_Factor)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['basket', 'send']
