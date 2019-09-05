from django import forms
from . import models
class PaymentForm(forms.Form):
    credit_card_number = forms.CharField(label='Número do Cartão de Crédito',
                                         widget=forms.NumberInput(attrs={'class': 'form-control', }))
    credit_card_cvv = forms.CharField(label='Código de segurança do Cartão',
                                      widget=forms.NumberInput(attrs={'class': 'form-control', }))

    credit_card_first_name = forms.CharField(label='Primeiro Nome(Igual ao Cartão)',widget=forms.TextInput(attrs={'class': 'form-control',}))
    credit_card_last_name = forms.CharField(label='Sobrenome(Igual ao Cartão)',widget=forms.TextInput(attrs={'class': 'form-control',}))
    credit_card_month = forms.CharField(label='Mes de Vencimento', widget=forms.TextInput(attrs={'class': 'form-control',}) )
    credit_card_year = forms.CharField(label='Ano de vencimento', widget=forms.TextInput( attrs={'class': 'form-control',} ))

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['shipment',]