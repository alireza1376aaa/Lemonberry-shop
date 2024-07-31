from django.urls import path
from .views import comment_page

app_name='comment_product'

urlpatterns = [

    path('comment',comment_page,name="commentform"),

]
