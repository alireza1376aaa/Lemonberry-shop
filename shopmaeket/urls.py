"""
URL configuration for shopmaeket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("account_shop.urls", namespace='account')),
    path('setting/', include("sitesetting.urls", namespace='setting')),
    path('product/', include("Product.urls", namespace='product')),
    path('', include("Home_page.urls")),
    path('favorite/', include('favorite_prducts.urls', namespace='favorite_product')),
    path('comment/', include('Product_details.urls', namespace='product_det')),
    path('cart/', include('shopping_cart.urls', namespace='shopping_cart')),
    path('Factor/', include('Send_and_Factor.urls', namespace='Factor')),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
