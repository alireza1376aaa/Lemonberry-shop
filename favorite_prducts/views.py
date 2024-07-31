from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from favorite_prducts.forms import favorite_form
from .models import favorite
from Product.models import Product_main_class
from django.contrib.auth.models import User


# Create your views here.

@login_required(login_url='/user/login')
def make_favorite(request):
    favorite_forms = favorite_form(request.POST or None)
    product_favarit_fild = request.POST.get('salam')

    if favorite_forms.is_valid():

        Product_id = favorite_forms.cleaned_data.get("product_id")
        product = Product_main_class.objects.get_by_id(product_id=Product_id)

        x = favorite.objects.filter(product_id=Product_id, owner_id=request.user.id)

        if x.exists():
            pass
        else:

            favorite.objects.create(owner_id=request.user.id, product_id=product.id)
    else:
        product = Product_main_class.objects.get_by_id(product_id=product_favarit_fild)

        x = favorite.objects.filter(product_id=product_favarit_fild, owner_id=request.user.id)

        if x.exists():
            pass
        else:

            favorite.objects.create(owner_id=request.user.id, product_id=product.id)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/user/login')
def favorite_page(request):
    contex = {'favoriteDitails': None}
    Favorite = favorite.objects.filter(owner_id=request.user.id)

    if Favorite is not None:
        contex['favoriteDitails'] = Favorite

    return render(request, 'favorite_page.html', contex)


@login_required(login_url='/user/login')
def remove_favorite(request, *args, **kwargs):
    x = request.POST.get('salam')
    y = request.POST.get('product_id')
    bool_rec = False
    if (x or y) is not None:
        bool_rec = True
    favorite_id = kwargs.get('favorite_id')
    if favorite_id is not None:
        if bool_rec:
            favorite_ditails = favorite.objects.filter(product_id=favorite_id, owner_id=request.user.id).first()
            if favorite_ditails is not None:
                favorite_ditails.delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            favorite_ditails = favorite.objects.filter(id=favorite_id, owner_id=request.user.id).first()
            if favorite_ditails is not None:
                favorite_ditails.delete()
                return redirect('/favorite')

    raise Http404()
