from django.forms import ModelForm
from django import forms
from sitesetting.models import contact_us


class creatform(ModelForm):
    class Meta:
        model = contact_us
        fields = ['fullname', 'subject', 'email', 'massege']
        widgets = {

            'fullname': forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی'}),
            'subject': forms.TextInput(attrs={'placeholder': 'موضوع'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
            'massege': forms.Textarea(attrs={'placeholder': 'پیغام'}),

        }
