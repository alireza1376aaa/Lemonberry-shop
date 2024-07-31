"""AG_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from .views import Home_Page, Search, collect_women_nav, collect_men_nav , collect_kids_nav

urlpatterns = [
    path('', Home_Page, name='home_page'),
    path('collect_women_nav', collect_women_nav, name='women_nav'),
    path('collect_men_nav', collect_men_nav, name='men_nav'),
    path('collect_kids_nav', collect_kids_nav, name='kids_nav'),

]
