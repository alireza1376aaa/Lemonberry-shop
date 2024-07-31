from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from .models import autentication


class register_form(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control mt-1", "placeholder": "ایمیل خود را وارد کنید"}),
        label="ایمیل")

    phone = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control mt-1", "placeholder": "شماره تلفن خود را وارد کنید"}),
        label="شماره همراه ", min_value=9000000000, max_value=9999999999,
        error_messages={'min_value': 'تعداد کاراکتر های شماره موبایل کم تر از حد مجاز میباشد',
                        'max_value': 'تعداد کاراکتر های شماره موبایل بیشتر تر از حد مجاز میباشد'})
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'id': 'password_fild', "class": "form-control mt-1", "placeholder": "رمز عبور خود را وارد کنید"}),
        label="رمز عبور")
    password_again = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control mt-1", "placeholder": "رمز عبور خود را وارد کنید"}),
        label="تکرار رمز عبور")

    def clean_password_again(self):
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password_again')

        if pass1 != pass2:
            raise forms.ValidationError("پسورد با هم تطابق ندارد")

    def clean_email(self):
        email = self.cleaned_data.get('email')

        checkuser = autentication.objects.filter(email__iexact=email)

        if checkuser.exists():
            raise forms.ValidationError("ایمیلی با همچین مشخصه ای موجود است")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        new_phone = f'+98{str(phone)}'
        checkuser = autentication.objects.filter(phone__iexact=new_phone)

        if checkuser.exists():
            raise forms.ValidationError("شماره همراهی با همچین مشخصه ای موجود است")
        return new_phone


class login_form(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control mt-1", "placeholder": "ایمیل"}), label="ایمیل")

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control mt-1", "placeholder": "رمز عبور"}), label="رمز عبور")


class edit_form(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control mt-1", "placeholder": "ایمیل خود را وارد کنید"}),
        label="ایمیل", required=True,error_messages={'required': 'پر کردن این فیلد اجباری میباشد'})

    phone = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control mt-1", "placeholder": "شماره تلفن خود را وارد کنید"}),
        label="شماره همراه ", min_value=9000000000, max_value=9999999999,
        error_messages={'min_value': 'تعداد کاراکتر های شماره موبایل کم تر از حد مجاز میباشد',
                        'max_value': 'تعداد کاراکتر های شماره موبایل بیشتر تر از حد مجاز میباشد',
                        'required': 'پر کردن این فیلد اجباری میباشد'}, required=True)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mt-1", "placeholder": "نام  خود را وارد کنید"}),
        label="نام", required=True,error_messages={'required': 'پر کردن این فیلد اجباری میباشد'})
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mt-1", "placeholder": "نام خانوادگی خود را وارد کنید"}),
        label="نام خانوادگی", required=True,error_messages={'required': 'پر کردن این فیلد اجباری میباشد'})
    image_pro = forms.FileField(
        widget=forms.FileInput(attrs={'id': 'profile_image', 'class': 'btn btn-primary', 'onchange': "readURL(this);",
                                      'accept': "image/jpeg, image/png"}), required=False)

    def clean_password_again(self):
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password_again')

        if pass1 != pass2:
            raise forms.ValidationError("پسورد با هم تطابق ندارد")

    def clean_email(self):
        email = self.cleaned_data.get('email')

        checkuser = autentication.objects.filter(email__iexact=email)
        cheak = checkuser.first()
        if checkuser.exists() and email != cheak.email:
            raise forms.ValidationError("ایمیلی با همچین مشخصه ای موجود است")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        new_phone = f'+98{str(phone)}'
        checkuser = autentication.objects.filter(phone__iexact=new_phone)
        cheak = checkuser.first()
        if checkuser.exists() and cheak.phone != new_phone:
            raise forms.ValidationError("شماره مبایلی با همچین مشخصه ای موجود است")
        return new_phone

    def clean_image_pro(self):
        image = self.cleaned_data.get('image_pro')

        if image is not None and image.size > 5000000:
            raise forms.ValidationError('سایز تصویر انتخابی بیشتر از حد مجاز است')
        return image

class forgetpass_form(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control mt-1", "placeholder": "ایمیل خود را وارد کنید"}),
        label="ایمیل",required=True,error_messages={'required':'پر کردن این فیلد اجباری است'})

    def clean_email(self):
        Email = self.cleaned_data.get('email')
        qu = autentication.objects.filter(email=Email)

        if qu.exists() == False:
            raise forms.ValidationError("ایمیلی با همچین مشخصه ای ثبت نام نکرده است")
        return Email


class forgetpass_form_edit(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control mt-1", "placeholder": "رمز عبور خود را وارد کنید"}),
        label="رمز عبور")

    password_again = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control mt-1", "placeholder": "رمز عبور خود را وارد کنید"}),
        label="تکرار رمز عبور",required=True,error_messages={'required':'پر کردن این فیلد اجباری است'})

    def clean_password_again(self):
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password_again')

        if pass1 != pass2:
            raise forms.ValidationError("پسورد با هم تطابق ندارد")

