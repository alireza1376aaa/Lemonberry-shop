from django import forms


class favorite_form(forms.Form):
    product_id = (forms.IntegerField(widget=forms.HiddenInput()))
