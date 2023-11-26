from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, label='Ім\'я')
    phone = forms.CharField(max_length=200, label='Телефон')
    address = forms.CharField(max_length=200, label='Адреса')
