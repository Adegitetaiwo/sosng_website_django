from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField(label='', max_length=128,
    widget= forms.EmailInput
    (attrs={'class':'subscribe_f', 'id':'subscribe_form', 'placeholder': 'Your Email Address'}))
