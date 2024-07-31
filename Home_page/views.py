from django.shortcuts import redirect, render
import itertools
from account_shop.send_email import send_email

# from Product_shop.models import product_shop
# from account_shop.forms import login_form
# from account_shop.views import Log_in
# from django.contrib.auth.models import User
#
# from collect_product.models import collect_product_main, collect_product, collect_product_type
from sitesetting.models import sitesetting, contact_us
from slider.models import slider, collection
from shopping_cart.models import Final_cart
from Home_page.form import khabarname_form
from django.contrib import messages
from Product.models import Product_main_class
from favorite_prducts.models import favorite
from product_inheritance.models import collect_product


# from django.conf import settings
# from django.core.mail import send_mail


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def Navigation(request, *args, **kwargs):
    sitesettings = sitesetting.objects.first()
    if request.user.is_authenticated:
        Order = Final_cart.objects.filter(user_id_id=request.user.id, is_pay=False).first() or None
        if Order is not None:
            lentotalwithtravel = len(Order.cart_set.all())
            context = {'order': Order, 'total': Order.total_price(), 'totalwithtravel': Order.total_price() + 30000,
                       'name': request.user.first_name, 'site': sitesettings, 'len': lentotalwithtravel}
        else:
            context = {'name': request.user.first_name, 'site': sitesettings, 'total': 0, 'len': 0}
    else:
        context = {'total': 0, 'site': sitesettings}

    return render(request, 'Main_template/Navigation.html', context)


def Footer(request, *args, **kwargs):
    forms_khabarname = khabarname_form(request.POST or None)

    if forms_khabarname.is_valid():
        Email = forms_khabarname.cleaned_data.get("email_khabar")
        subject = 'خوش آمدید به خبرنامه ما'
        if request.user.is_authenticated:
            send_email('خوش آمدید به خبرنامه ما', str(request.user.email), {'data': request.user.get_full_name()},
                       'email/news.html')
        else:
            messages.warning(request, 'ابتدا ثبت نام کنید ')

    sitesettings = sitesetting.objects.first()

    kwargs['site'] = sitesettings
    kwargs['register_form'] = forms_khabarname
    return render(request, 'Main_template/Footer.html', kwargs)


def Search(request, *args, **kwargs):
    return render(request, 'Main_template/__search_templates.html', {})


def Home_Page(request, *args, **kwargs):
    sliders = slider.objects.all()
    collections = collection.objects.first()

    Special_product = Product_main_class.objects.filter(product_active=True, product_type='discount',
                                                        count__isnull=False).order_by('-price_discount').distinct().all()[:6]

    new_product = Product_main_class.objects.filter(product_active=True, product_type='discount',
                                                    count__isnull=False).order_by('-product_date').all().distinct()
    main_commet = contact_us.objects.filter(is_read=True, user_id__isnull=False).order_by('-date')
    views_product = Product_main_class.objects.filter(product_active=True, product_type='discount',
                                                      count__isnull=False).order_by('-product_visit').all().distinct()
    collect_favorite = list(
        favorite.objects.filter(owner_id=request.user.id).values_list('product_id', flat=True).distinct())
    context = {'sliders': sliders,
               'collection_slider': collections,
               'Special': Special_product,
               'new_product': new_product,
               'views': views_product,
               'collect_favorite': collect_favorite,
               'main_commet': main_commet
               }

    return render(request, 'Home_page.html', context)


def collect_men_nav(request, **kwargs):
    collect_main = collect_product.objects.filter(parent=None)

    contex = {'collect_main': collect_main, 'select_gender': [None, 'men']}

    return render(request, 'navigation/nav_men.html', contex)


def collect_women_nav(request, **kwargs):
    collect_main = collect_product.objects.filter(parent=None)

    contex = {'collect_main': collect_main, 'select_gender': [None, 'women']}

    return render(request, 'navigation/nav_women.html', contex)


def collect_kids_nav(request, **kwargs):
    collect_main = collect_product.objects.filter(parent=None)

    contex = {'collect_main': collect_main, 'select_gender': [None, 'kids']}

    return render(request, 'navigation/nav_kids.html', contex)
