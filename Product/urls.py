# from django.conf.urls import url
from django.urls import path, include
from .views import list_view_men, search, product_detail, count_color

app_name = 'Product'

urlpatterns = [

    # list view ------------------------------------------------------------
    path('list_view/<str:gender>/<str:cat>', list_view_men, name="list_view_men"),

    # details view ------------------------------------------------------------
    path('list_view/<str:cat>/<slug>/<productId>', product_detail, name="details_view"),
    # search ------------------------------------------------------------
    path('list_view/search', search.as_view(), name='search_product'),

    path('get_color_product', count_color)
]
