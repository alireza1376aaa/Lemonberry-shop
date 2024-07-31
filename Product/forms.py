from django import forms


class paginatorss(forms.Form):
    page_num = forms.ChoiceField(choices=[(6, 6), (12, 12), (24, 24), (48, 48)], label='', initial=6)
    filter_pro = forms.ChoiceField(
        choices=[(1, "اسم محصول"), (2, "محبوب ترین ها"), (3, "قیمت از زیاد به کم"), (4, "قیمت از کم به زیاد"),
                 (5, "اخرین محصولات")], label='', initial='مرتب سازی')
