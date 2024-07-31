from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .forms import order_form, finallyorder_form
from .models import Final_cart, Cart, finally_order
from Product.models import Product_main_class
from account_shop.models import autentication
from .datetime import timedatePersian
from django.contrib import messages
from Product_details.models import Count
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from account_shop.send_email import send_email
import datetime
from Send_and_Factor.models import Send_Factor
from shopping_cart.number_to_words import convert


def single_cart(request):
    Product_id = request.POST.get('productid_small') or None
    count_reposit = request.POST.get('count_reposit') or None
    count = int(request.POST.get("count_small")) or None
    if (Product_id and count_reposit and count) is not None:
        mycount = Count.objects.filter(Product_main_class_id=Product_id, id=count_reposit, count_pro__gt=0).first()

        if request.user.is_authenticated:
            if mycount.count_pro < count:
                messages.error(request, 'این تعداد محصول موجود نمیباشد')

            elif count == 0:
                messages.error(request, ' تعداد محصول وارد شده صجیح نمیباشد')

            else:
                select_product = Product_main_class.objects.filter(id=Product_id).first()
                if select_product is not None:
                    basket_cart, created = Final_cart.objects.get_or_create(is_pay=False, user_id_id=request.user.id)
                    basket_cart_detail = basket_cart.cart_set.filter(product_id_id=Product_id,
                                                                     color_size=mycount).first()
                    if basket_cart_detail is not None:
                        basket_cart_detail.count += count
                        basket_cart_detail.save()
                    else:
                        new_detail = Cart(final_cart_id=basket_cart.id, product_id_id=Product_id, count=count,
                                          color_size=mycount)
                        new_detail.save()

                    messages.success(request, 'محصول مورد نظر با موفقیت به سبد خرید اضافه شد')

                else:
                    messages.error(request, 'محصول مورد نظر یافت نشد')
        else:
            messages.warning(request, 'برای ثبت سفارش می باید ثبت نام کنید')

    else:
        messages.error(request, 'برای ثبت محصول مورد نظر مشکلی پیش امده')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def cart(request):
    order_forms = order_form(request.POST or None)
    if order_forms.is_valid():
        Product_id = order_forms.cleaned_data.get("product_id")
        count_repository_size = request.POST.get('count_repo_size')
        count_repository_color = request.POST.get('count_repo_color')
        count = order_forms.cleaned_data.get("count")
        mycount = Count.objects.filter(Product_main_class_id=Product_id, product_size_id=count_repository_size,
                                       product_color_id=count_repository_color, count_pro__gt=0).first()

        if request.user.is_authenticated:

            if mycount.count_pro < count:
                messages.error(request, 'این تعداد محصول موجود نمیباشد')

            elif count == 0:
                messages.error(request, ' تعداد محصول وارد شده صجیح نمیباشد')

            else:
                select_product = Product_main_class.objects.filter(id=Product_id).first()
                if select_product is not None:
                    basket_cart, created = Final_cart.objects.get_or_create(is_pay=False, user_id_id=request.user.id)
                    basket_cart_detail = basket_cart.cart_set.filter(product_id_id=Product_id,
                                                                     color_size=mycount).first()
                    if basket_cart_detail is not None:
                        basket_cart_detail.count += count
                        basket_cart_detail.save()
                    else:
                        new_detail = Cart(final_cart_id=basket_cart.id, product_id_id=Product_id, count=count,
                                          color_size=mycount)
                        new_detail.save()

                    messages.success(request, 'محصول مورد نظر با موفقیت به سبد خرید اضافه شد')

                else:
                    messages.error(request, 'محصول مورد نظر یافت نشد')
        else:
            messages.warning(request, 'برای ثبت سفارش می باید ثبت نام کنید')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required(login_url='/user/login')
def shopping_cart_page(request):
    myorder = Final_cart.objects.prefetch_related('cart_set').filter(
        is_pay=False, user_id_id=request.user.id).first() or None
    if myorder is not None:
        final_price = myorder.total_price()
        if final_price < 500000:
            final_price = myorder.total_price_with_delivery()
        context = {'order': myorder, 'total': final_price}
    else:
        context = {}
    return render(request, 'basket_page.html', context)


@login_required(login_url='/user/login')
def remove_order_detail(request, detail_id):
    rm_product = int(detail_id) or None
    if rm_product is not None:

        delet_cart = Cart.objects.filter(id=rm_product, final_cart__user_id_id=request.user.id) or None
        if delet_cart is not None:
            delet_cart = delet_cart.delete()
            messages.warning(request, 'محصول موردنظر از سبد خرید شما حذف شد')

        else:
            messages.error(request, 'محصول مورد نظر یافت نشد')

    else:
        messages.error(request, 'محصول مورد نظر یافت نشد')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='/user/login')
def change_order_detail(request):
    product_id = int(request.GET.get('detail_id'))
    status = request.GET.get('status')

    change_count_cart = Cart.objects.filter(product_id_id=product_id, final_cart__user_id_id=request.user.id,
                                            final_cart__is_pay=False).first()
    if status == 'plus':
        change_count_cart.count += 1
        change_count_cart.save()
    elif status == 'minus':
        change_count_cart.count -= 1
        if change_count_cart.count == 0:
            change_count_cart.delete()
        else:
            change_count_cart.save()

    myorder, boolorder = Final_cart.objects.prefetch_related('cart_set').get_or_create(
        is_pay=False, user_id_id=request.user.id)
    final_price = myorder.total_price()
    if final_price < 500000:
        final_price = myorder.total_price_with_delivery()
    context = {'order': myorder, 'total': final_price}

    return JsonResponse({'body': render_to_string('include/include_shoping_cart.html', context)})


@login_required(login_url='/user/login')
def shopping_cart_finally_page(request):
    user = autentication.objects.get(id=request.user.id)
    addres = finally_order.objects.filter(user=user).first() or None
    myorder = Final_cart.objects.prefetch_related('cart_set').filter(
        is_pay=False, user_id_id=request.user.id).first() or None

    if myorder is None:
        return redirect('shopping_cart:carts')

    if addres is not None:
        form = finallyorder_form(request.POST or None,
                                 initial={'fullname': user.get_full_name(), 'phone': '0' + str(user.phone)[3:],
                                          'address': addres.address, 'post_code': addres.post_code, 'city': addres.city,
                                          'city_location': addres.city_location, 'factor_code': myorder.Order_number}, )
    else:
        form = finallyorder_form(request.POST or None,
                                 initial={'fullname': user.get_full_name(), 'phone': '0' + str(user.phone)[3:],
                                          'factor_code': myorder.Order_number}, )
    today = timedatePersian.today_date

    for check_count in myorder.cart_set.all():
        count_check = int(check_count.color_size.count_pro) - int(check_count.count)

        if count_check < 0:
            check_count.count = check_count.color_size.count_pro
            new_count = Cart.objects.filter(id=check_count.id).update(count=check_count.color_size.count_pro)
            messages.error(request,
                           f'محصول {check_count.color_size.Product_main_class.product_name} به رنگ {check_count.color_size.product_color.product_color} سایز {check_count.color_size.product_size.product_size} بدین تعداد در انبار موجود نمیباشد به صورت خودکار تعداد محصول تنظیم میشود')

    final_price = myorder.total_price()
    if final_price < 500000:
        final_price = myorder.total_price_with_delivery()
    context = {'order': myorder, 'total': final_price, 'form': form, 'date': today}
    if form.is_valid():
        form.save(user)
        myorder.code_tr = get_random_string(30)
        myorder.save()
        send_email('نهایی کردن پرداخت', str(user.email), {'data': myorder.code_tr}, 'email/verify_pay.html')

        messages.success(request, 'شما به درگاه پرداخت انقال پیدا میکنید')

    return render(request, 'finally_basket_page.html', context)


@login_required(login_url='/user/login')
def request_payment(request, code):
    position_pay = code
    if position_pay is not None:
        myorder = Final_cart.objects.filter(is_pay=False, user_id_id=request.user.id).first()

        if position_pay == myorder.code_tr:
            myorder.is_pay = True
            myorder.date = datetime.datetime.now()
            send_class = Send_Factor.objects.create(basket=myorder, send=False)

            for count_repository in myorder.cart_set.all():
                count = count_repository.count
                color_size_id = count_repository.color_size.id
                new_count = int(count_repository.color_size.count_pro) - int(count)
                new_count = Count.objects.filter(id=color_size_id).update(count_pro=new_count)
                if count_repository.product_id.price_discount > 0:
                    final_cart = Cart.objects.filter(id=count_repository.id).update(
                        final_price=count_repository.product_id.product_price,
                        final_price_discount=count_repository.product_id.price_discount)
                else:
                    final_cart = Cart.objects.filter(id=count_repository.id).update(
                        final_price=count_repository.product_id.product_price)
            myorder.save()
            context = {'order': myorder}
            return render(request, 'success-order.html', context)
        else:
            messages.error(request, 'پراخت صورت نگرفت دوباره تلاش کنید')
            return redirect('shopping_cart:finallt_carts')
    else:
        messages.error(request, 'پرداخت به صورت موفقیت امیز نبود')
        return redirect('shopping_cart:finallt_carts')


@login_required(login_url='/user/login')
def old_cart_page(request):
    order = Final_cart.objects.filter(is_pay=True, user_id=request.user).all().order_by('-date')
    context = {'main_oreder': order}
    return render(request, 'old_basket.html', context)


@login_required(login_url='/user/login')
def show_factor(request, code_factor):
    order = Final_cart.objects.filter(is_pay=True, user_id=request.user, Order_number=code_factor).first() or None
    if order is not None:
        send = Send_Factor.objects.filter(basket=order).first()
        addres = finally_order.objects.filter(user=request.user,factor_code=code_factor).first()
        takhfif = int(order.total_price_without_discount() - order.total_price())
        work_number = convert(str(order.total_price_with_delivery()))
        context = {'data': order, 'send': send, 'addres': addres, 'takhfif': takhfif, 'work_number': work_number}
        return render(request, 'factor/Factor.html', context)
    else:
        raise Http404()
