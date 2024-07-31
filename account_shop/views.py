from django.contrib.auth import login, logout
from .send_email import send_email
from .forms import register_form, login_form, edit_form, forgetpass_form, forgetpass_form_edit
from django.shortcuts import render, redirect, Http404, HttpResponse
from .models import autentication
import random


def Register_User(request):
    if request.user.is_authenticated:
        return redirect('account:Edit')
    forms_register = register_form(request.POST or None)

    try:
        forms_register.initial = {'email': request.session['email'] or None,
                                  'phone': '0' + request.session['phone'][3:] or None}
    except:
        pass

    context = {"register_form": forms_register}
    send_again_code = request.GET.get('again')
    if send_again_code == 'True':
        random_code = random.randint(10000, 99999)
        send_email('verify_acount', request.session['email'], {'data': random_code}, 'email/verify.html')
        request.session['random_code'] = random_code

    if request.method == "POST":

        if forms_register.is_valid():
            email = forms_register.cleaned_data.get("email")
            phone = forms_register.cleaned_data.get("phone")
            password = forms_register.cleaned_data.get("password")
            random_code = random.randint(10000, 99999)
            send_email('فعال کردن حساب کاربری', str(email), {'data': random_code}, 'email/verify.html')
            request.session['email'] = email
            request.session['phone'] = phone
            request.session['password'] = password
            request.session['random_code'] = random_code
            return render(request, "account/verify.html", context)

        verify = request.POST.get('code')

        if verify is not None:

            if verify == str(request.session['random_code']):
                new_user = autentication.objects.create_user(email=request.session['email'],
                                                             password=request.session['password'],
                                                             phone=request.session['phone'],
                                                             verify_code=random.randint(1000000, 9999999))
                login(request, new_user)
                return HttpResponse('ok', status=200)
            else:
                return HttpResponse('bad', status=400)

    return render(request, "account/Register_page.html", context)


def Log_in(request):
    if request.user.is_authenticated:
        return redirect('account_shop:Edit')
    forms = login_form(request.POST or None)
    try:
        forms.initial = {'email': request.session['email'], 'password': request.session['password']}
    except:
        pass
    context = {"form": forms, 'massage': None}

    try:
        pathurl = request.META.get('HTTP_REFERER')
        oldurl = pathurl.split('/')
        if oldurl[4] == 'forget_pass' and len(oldurl) == 5:
            context['massage'] = 'ایمیل به شما با موفقیت ارسال شد'

        if len(oldurl) >= 6 and oldurl[3] != 'product':
            context['massage'] = 'کلمه عبور  شما با موفقیت تغیر پیدا کرد'
    except:
        pass

    if forms.is_valid():
        email = forms.cleaned_data.get("email")
        Password = forms.cleaned_data.get("password")
        user = autentication.objects.filter(email=email).first()
        remember = request.POST.get('remember_me')
        if user is not None:
            if user.check_password(Password):
                login(request, user)
                return redirect('account:Edit')
            else:
                forms.add_error('password', 'رمز عبور به درستی وارد نشده')

            if remember == 'on':
                request.session['email'] = email
                request.session['password'] = Password
            else:
                pass

        else:
            forms.add_error("email", "کاربری با این نام کاربری موجود نیست")

    return render(request, 'account/Log_in.html', context)


def Log_out(request):
    logout(request)
    return redirect("account:login")


def Edit_user(request):
    user_id = request.user.id
    try:
        user = autentication.objects.get(id=user_id)
    except:
        raise Http404("کاربری با این مشخصه یافت نشد")

    edit_user = edit_form(request.POST or None, request.FILES or None,
                          initial={'email': user.email, 'phone': '0' + str(user.phone)[3:],
                                   'first_name': user.first_name,
                                   'last_name': user.last_name, 'image_pro': None})
    if edit_user.is_valid():
        phone = edit_user.cleaned_data.get('phone')
        first_name = edit_user.cleaned_data.get('first_name')
        last_name = edit_user.cleaned_data.get('last_name')
        email = edit_user.cleaned_data.get('email')
        image_pro = edit_user.cleaned_data['image_pro']

        user.phone = phone
        user.first_name = first_name
        user.last_name = last_name
        if email != user.email:
            user.email = email
            user.is_verify = False
        if image_pro is not None:
            user.image_pro = image_pro
        user.save()

    contex = {"edit_form": edit_user, 'user': user}
    return render(request, 'account/edit_page.html', contex)


def forget_pass(request):
    my_form = forgetpass_form(request.POST or None)

    if my_form.is_valid():
        email_myform = my_form.cleaned_data.get('email')
        user = autentication.objects.filter(email=email_myform).first()
        send_email('فراموشی رمز عبور', str(email_myform), {'code': user.verify_code}, 'email/forgetpass.html')
        return redirect('account:login')

    contex = {'my_form': my_form}
    return render(request, 'forgot_password/password_reset_email.html', contex)


def forget_pass_reset(request, code):
    urlcode = code
    user = autentication.objects.filter(verify_code=urlcode).first()
    if user is None:
        raise Http404("کاربری با این مشخصه یافت نشد")

    passform = forgetpass_form_edit(request.POST or None)

    if passform.is_valid():
        password = passform.cleaned_data.get('password')
        user.set_password(password)
        user.verify_code = random.randint(1000000, 9999999)
        user.save()
        return redirect('account:login')

    contex = {"edit_form": passform}

    return render(request, 'forgot_password/reset_passs.html', contex)
