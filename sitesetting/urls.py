from django.urls import path
from sitesetting.views import contact_us_page, privacy_page, rules_page

app_name = "sitesetting"

urlpatterns = [
    path('contact_us', contact_us_page, name="contact_us_form"),
    path('privacy_page', privacy_page, name="privacy_page"),
    path('rules_page', rules_page, name="rules_page"),
]
