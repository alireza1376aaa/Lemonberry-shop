from django.contrib import admin
from sitesetting.models import sitesetting, contact_us ,extra_setting


# Register your models here.

class filter_contact(admin.ModelAdmin):
    list_display = ['__str__', 'subject']

    class meta:
        model = contact_us


admin.site.register(contact_us, filter_contact)
admin.site.register(sitesetting)
admin.site.register(extra_setting)
