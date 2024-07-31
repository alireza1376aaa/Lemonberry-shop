import itertools

from django.db.models import Q
from django.views.generic import ListView

from Product.forms import paginatorss
# from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, HttpResponse, Http404
# from Product_shop.models import product_shop, collect_product, product_gallery
# from django.views.generic import ListView, DetailView
# # Create your views here.
# # from tag_shop.models import tag_product
# from collect_product.models import collect_product_type, collect_product, collect_product_main
from shopping_cart.forms import order_form
from favorite_prducts.forms import favorite_form
from django.core.paginator import Paginator
# from ditails_product.models import color, size
# from tag_shop.models import tag_product
# from comment_product.forms import commentform
# from comment_product.models import comment
from .models import size, brand, color, Product_main_class, tag_product, collect_product, extra_discription
import re
from Product_details.models import Count, product_gallery, comment
from Product_details.forms import commentform
from favorite_prducts.models import favorite


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def cheak_order(order):
    if order == 'product_name':
        order = '1'
    elif order == '-product_name':
        order = '2'
    elif order == '-product_price':
        order = '3'
    elif order == 'product_price':
        order = '4'
    elif order == '-product_date':
        order = '5'
    return order


def list_view_men(request, gender, cat):
    if gender in ['men', 'women', 'kids']:
        order = request.GET.get('filter_pro') or '-product_date'
        initial_order = cheak_order(order)
        path = ''
        active = ''
        page1 = 6
        filter_val = request.GET.get('check_filter')
        form = paginatorss(request.POST or None, initial={'filter_pro': initial_order})
        cx = ''
        if form.is_valid():
            page1, order = get_filter_sample(form)
            cx = f'&filter_pro={order}&page_num={page1}'

        # ///////////////// db /////////////////////////////
        collect_favorite = list(
            favorite.objects.filter(owner_id=request.user.id).values_list('product_id', flat=True).distinct())
        data = Product_main_class.objects.filter(product_active=True, count__isnull=False,
                                                 product_gender=gender).distinct()
        if cat != 'all':
            data = data.filter(Q(collect_products__parent__name_collect_product_main=cat) |
                               Q(collect_products__parent__parent__name_collect_product_main=cat) |
                               Q(collect_products__name_collect_product_main=cat))

        try:
            old_path = request.get_full_path_info()
            path_old = str(old_path.split('?')[1]) + cx
            path = re.sub('page=\d&', '', path_old)

        except:
            pass

        if filter_val is not None:
            data_filter, active = get_filter(data, request)

        else:
            data_filter = data

        paginator = Paginator(data_filter.order_by(order), page1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        filter_fild = filter_men(data or None, gender)
        context = {'form': form, 'page_obj': page_obj, 'path': path, 'active': active,
                   'collect_favorite': collect_favorite}
        context |= filter_fild

        return render(request, 'products/List_view/List_view_men.html', context)
    else:
        return Http404()


def get_filter(data_db, request):
    type = request.GET.getlist('type') or None
    brand = request.GET.getlist('brand') or None
    price = request.GET.getlist('price') or None
    color = request.GET.getlist('color') or None

    active = {}
    data = data_db

    if type is not None:
        data = data.filter(collect_products_id__in=type).all()
        active['type'] = list(map(int, type))
    if brand is not None:
        data = data.filter(product_brand_id__in=brand).all()
        active['brand'] = list(map(int, brand))

    if price is not None:
        min_price = price[0].split(',')[0]
        max_price = price[-1].split(',')[1]
        data = data.filter(product_price__gte=min_price, product_price__lte=max_price).all()
        # active['price'] = [eval(i) for i in price]
        activex = []
        for i in price:
            xc = i.split(',')
            activex.append(int(max(xc)))
        active['price'] = activex

    if color is not None:
        data = data.filter(count__product_color_id__in=color).all()
        active['color'] = list(map(int, color))

    return data, active


def get_filter_sample(form):
    page1 = form.cleaned_data.get('page_num')
    order_filter_number_them = form.cleaned_data.get('filter_pro')
    if order_filter_number_them == '1':
        order = 'product_name'
    elif order_filter_number_them == '2':
        order = '-product_name'
    elif order_filter_number_them == '3':
        order = '-product_price'
    elif order_filter_number_them == '4':
        order = 'product_price'
    elif order_filter_number_them == '5':
        order = '-product_date'

    return page1, order


def price_filter_set(data_db):
    data = data_db
    min_price = data.order_by('product_price').values('product_price').first()
    max_price = data.order_by('-product_price').values('product_price').first()
    z = int(max_price['product_price'])
    w = int(min_price['product_price'])
    number = (int(z) - int(w)) / 5
    val_price = dict()

    if number == 0.0:
        val_price = {1: {0, z}}

    else:
        for i in range(1, 6):
            val_price[i] = {round(int(w + ((i - 1) * number))),
                            (round(int(w + (i * number)))) if i == 5 else (round(int(w + (i * number))))}
    return val_price


def filter_men(data, slected_gender):
    if data is None:
        collect_type = collect_product.objects.filter(parent=None)
        select_gender = [None, slected_gender]

        return {'collect_type': collect_type, 'select_gender': select_gender}
    collect_type = collect_product.objects.filter(parent=None)

    # /////////////////////////////////////////////////////////////////
    da = data.values('count__product_color_id', 'count__product_color__product_color').distinct()
    color = da

    # /////////////////////////////////////////////////////////////////
    db = data.values('product_brand_id', 'product_brand__product_brand').distinct()
    brands = db

    sugest = data.order_by('-product_date').all()[:3]
    val_price = price_filter_set(data)

    dc = data.values('collect_products_id', 'collect_products__title_collect_product_main').distinct()
    collect = dc
    select_gender = [None, slected_gender]
    context = {'collect': collect, 'collect_type': collect_type, 'colors': color, 'brand': brands, 'sugest': sugest,
               'price': val_price, 'select_gender': select_gender}
    return context


def product_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productId']
    order_forms = order_form(request.POST or None, initial={'product_id': selected_product_id})
    favorite_forms = favorite_form(request.POST or None, initial={'product_id': selected_product_id})
    order_forms_comment = commentform(request.POST or None, initial={'product_id': selected_product_id})

    product = Product_main_class.objects.get_by_id(int(selected_product_id))
    favorite_bool = favorite.objects.filter(product=product, owner_id=request.user.id).exists()
    collect_favorite = list(
        favorite.objects.filter(owner_id=request.user.id).values_list('product_id', flat=True).distinct())
    if product is None or not product.product_active:
        raise Http404('محصول مورد نظر یافت نشد')

    count = Count.objects.filter(Product_main_class=product, count_pro__gt=0).values('product_size',
                                                                                     'product_size__product_size',
                                                                                     'product_size__product_unit').distinct()
    sugest = Product_main_class.objects.get_queryset().filter(
        Q(collect_products=product.collect_products), ~Q(product_name=product.product_name),
        count__isnull=False).distinct()[:12]
    grouped_galleries_sugest = list(my_grouper(4, sugest))

    tag = product.tags
    galleries = product_gallery.objects.filter(Product_main_class=product)
    comment_massage = comment.objects.filter(product_id=product)
    len_massage = len(comment_massage)

    grouped_galleries = list(my_grouper(3, galleries))

    if request.user.is_authenticated:
        product.product_visit += 1
        product.save()

    context = {
        'object': product,
        'favorite_check': favorite_bool,
        'grouped_gallery': grouped_galleries,
        'sugest': grouped_galleries_sugest,
        'tag': tag,
        'basket': order_forms,
        'favorite': favorite_forms,
        'comment_form': order_forms_comment,
        'collect_favorite': collect_favorite,
        'color_size': count,
        'comment_massage': comment_massage.filter(parent=None).order_by('-data'),
        'len_massage': len_massage,
    }

    return render(request, 'products/Detail_view.html', context)


def count_color(request):
    count_repo = request.GET.get('count_repo') or None
    product_id = request.GET.get('product_id') or None
    data = ''
    if count_repo is not None:
        data = Count.objects.filter(product_size_id=count_repo, Product_main_class_id=product_id,
                                    count_pro__gt=0).values('product_color', 'product_color__product_color').distinct()
    context = {'custom_color': data}
    return render(request, 'products/include/color_include.html', context)


class search(ListView):
    paginate_by = 6
    template_name = 'products/List_view/List_view_men.html'

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product_main_class.objects.search(query)

        return Product_main_class.objects.get_product_active()
