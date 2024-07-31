from django.shortcuts import render
from sitesetting.models import sitesetting, contact_us, extra_setting
from sitesetting.forms import creatform
from account_shop.models import autentication


# Create your views here.


def contact_us_page(request):
    forms = creatform(request.POST or None)
    sitesettings = sitesetting.objects.first()
    context = {"form": forms, "object": sitesettings, 'massage': ''}

    if forms.is_valid():
        Fullname = forms.cleaned_data.get('fullname')
        Subject = forms.cleaned_data.get('subject')
        Email = forms.cleaned_data.get('email')
        Massege = forms.cleaned_data.get('massege')

        user = autentication.objects.filter(email=Email).first()
        if user is not None:
            contact_us.objects.create(user=user, fullname=Fullname, subject=Subject, email=Email, massege=Massege)
        else:
            contact_us.objects.create(fullname=Fullname, subject=Subject, email=Email, massege=Massege)
        context['massage'] = 'پیام شما با موفقیت ارسال شد'
        forms = creatform()

    return render(request, "contact_us.html", context)


def privacy_page(request):
    privacy_mypage = extra_setting.objects.first()
    privacy = ''
    if privacy_mypage is not None:
        privacy = privacy_mypage.privacy_text
    return render(request, 'Privacy.html', {'privacy': privacy})


def rules_page(request):
    rules_mypage = extra_setting.objects.first()
    rules = ''
    if rules_mypage is not None:
        rules = rules_mypage.ruls_text
    return render(request, 'rules.html', {'rules': rules})
