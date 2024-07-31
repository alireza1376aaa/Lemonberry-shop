from django.urls import path
from shopping_cart.views import show_factor
from .views import Show_list_factor,show_factor_admin

app_name = "Send_and_Factor"

urlpatterns = [
    path('Factor/<str:code_factor>', show_factor, name="Factor_form"),
    path('list_factor', Show_list_factor.as_view(), name="list_factor"),
    path('Factor_details/<str:code_factor>', show_factor_admin, name="show_factor"),

]
