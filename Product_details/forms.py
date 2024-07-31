from django.forms import ModelForm
from django import forms
from .models import comment


class commentform(ModelForm):
    choice = [
        ('', 'موضوع'), ('راضی هستم از خرید', 'راضی هستم از خرید'), ('راضی نیستم از خرید', 'راضی نیستم از خرید'),
        ('خرید نکردم', 'خرید نکردم'), ('پیشنهاد میکنم', 'پیشنهاد میکنم'), ('پیشنهاد نمیکنم', 'پیشنهاد نمیکنم'),
        ('معمولی بود', 'معمولی بود'), ('سوال دارم', 'سوال دارم')]
    subject = forms.ChoiceField(choices=choice, widget=forms.Select(attrs={'class': 'text-center formsub'}))

    class Meta:
        model = comment
        fields = ['subject', 'massege', 'product_id', 'parent']
        widgets = {
            'massege': forms.Textarea(attrs={'placeholder': 'پیغام'}),
            'product_id': forms.HiddenInput,
            'parent': forms.HiddenInput(attrs={'id':'parent_id_val'})

        }
