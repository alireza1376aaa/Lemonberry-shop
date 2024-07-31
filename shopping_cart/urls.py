from django.urls import path, include
from shopping_cart.views import cart, single_cart, shopping_cart_page, remove_order_detail, change_order_detail, \
    shopping_cart_finally_page, request_payment, old_cart_page

app_name = 'shopping_cart'

urlpatterns = [

    path('makecarts', cart, name="basket"),
    path('makecarts/single', single_cart, name="single_basket"),
    path('cart_page', shopping_cart_page, name="carts"),
    path('remove_order/<detail_id>', remove_order_detail, name='remove'),
    path('change-order-detail/', change_order_detail, name='change-order-detail'),
    path('finallt_carts', shopping_cart_finally_page, name="finallt_carts"),
    path('finallt_carts/<code>', request_payment, name="verify_finallt_carts"),
    path('old_basket_cart', old_cart_page, name="old_carts"),

]
