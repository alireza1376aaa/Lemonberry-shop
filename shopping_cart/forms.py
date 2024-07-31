from django import forms
from shopping_cart.models import finally_order


class order_form(forms.Form):
    product_id = (forms.IntegerField(widget=forms.HiddenInput(attrs={'id': 'product_my_id'})))
    count = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-text qty', 'id': 'qty1'}), initial=1,
                               min_value=1)


class finallyorder_form(forms.ModelForm):
    class Meta:
        City_select = (
            ("0", 'لطفا استان را انتخاب نمایید'),
            ("تهران", 'تهران'),
            ("گیلان", 'گیلان'),
            ("آذربایجان شرقی", 'آذربایجان شرقی'),
            ("خوزستان", 'خوزستان'),
            ("فارس", 'فارس'),
            ("اصفهان", 'اصفهان'),
            ("خراسان رضوی", 'خراسان رضوی'),
            ("قزوین", 'قزوین'),
            ("سمنان", 'سمنان'),
            ("قم", 'قم'),
            ("مرکزی", 'مرکزی'),
            ("زنجان", 'زنجان'),
            ("مازندران", 'مازندران'),
            ("گلستان", 'گلستان'),
            ("اردبیل", 'اردبیل'),
            ("آذربایجان غربی", 'آذربایجان غربی'),
            ("همدان", 'همدان'),
            ("کردستان", 'کردستان'),
            ("کرمانشاه", 'کرمانشاه'),
            ("لرستان", 'لرستان'),
            ("بوشهر", 'بوشهر'),
            ("کرمان", 'کرمان'),
            ("هرمزگان", 'هرمزگان'),
            ("چهارمحال و بختیاری", 'چهارمحال و بختیاری'),
            ("یزد", 'یزد'),
            ("سیستان و بلوچستان", 'سیستان و بلوچستان'),
            ("ایلام", 'ایلام'),
            ("کهگلویه و بویراحمد", ' کهگلویه و بویراحمد'),
            ("خراسان شمالی", 'خراسان شمالی'),
            ("خراسان جنوبی", 'خراسان جنوبی'),
            ("البرز", 'البرز'),
        )
        model = finally_order
        fields = ['fullname', 'phone', 'address', 'post_code', 'city', 'city_location', 'factor_code']
        required = ['address', 'post_code', 'city', 'city_location']
        error_messages = {
            'fullname': {'required': "پر کردن این فیلد اجباری است"},
            'phone': {'required': "پر کردن این فیلد اجباری است"},
            'address': {'required': "پر کردن این فیلد اجباری است"},
            'post_code': {'required': "پر کردن این فیلد اجباری است"},
            'city': {'required': "پر کردن این فیلد اجباری است"},
            'city_location': {'required': "پر کردن این فیلد اجباری است"}

        }
        widgets = {
            'fullname': forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی'}),
            'phone': forms.TextInput(attrs={'placeholder': 'تلفن'}),
            'address': forms.TextInput(attrs={'placeholder': 'آدرس'}),
            'post_code': forms.TextInput(attrs={'placeholder': 'کد پستی'}),
            'city_location': forms.Select(choices=City_select,
                                          attrs={'class': 'form-control text-center', 'placeholder': 'استان',
                                                 'onChange': 'irancitylist(this.value);', 'id': 'location'}),
            'city': forms.Select(attrs={'placeholder': 'شهر', 'id': "city", 'class': 'form-control text-center'}),
            'factor_code': forms.HiddenInput

        }

    def save(self, commit=True):
        instance = super(finallyorder_form, self).save(commit=False)
        instance.user = commit
        instance.save()

        return instance
