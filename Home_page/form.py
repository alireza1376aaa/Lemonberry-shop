from django import forms


class khabarname_form(forms.Form):
    email_khabar = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control mt-1", "placeholder": "ایمیل خود را وارد کنید"}),
        label="")
