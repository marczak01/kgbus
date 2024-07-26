from django.utils.translation import gettext_lazy as _
from django import forms

class EmailContactForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': "input form-top--item", 'placeholder': _('IMIĘ I NAZWISKO')}))
    email = forms.EmailField( widget=forms.TextInput(attrs={'class': "input form-top--item", 'placeholder': _('EMAIL')}))
    phone = forms.CharField(max_length=20,  widget=forms.TextInput(attrs={'class': "input input-block", 'placeholder': _('NUMER TELEFONU')}))
    message = forms.CharField(required=False,
                                widget=forms.Textarea(attrs={'class': "input input-block", 'placeholder': _('WIADOMOŚĆ'), 'rows': 7 }))