from django import forms
from . import models
class Product(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'category', 'price', 'short_description', 'description', 'quantity', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'inputs form-control',}),
            'price': forms.NumberInput(attrs={'class': 'inputs form-control',}),
            'category': forms.Select(attrs={'class': 'inputs form-control',}),
            'short_description': forms.TextInput(attrs={'class': 'text form-control', }),
            'description': forms.Textarea(attrs={'class': 'text form-control', }),
            'quantity': forms.NumberInput(attrs={'class': 'text form-control', }),
            'status': forms.Select(attrs={'class': 'text form-control', })
        }

class ProductQuestion(forms.ModelForm):
    class Meta:
        model = models.ProductQuestion
        fields = ['question', ]
        widgets = {
            'question': forms.Textarea(attrs={'class': 'inputs form-control'}),

        }
        labels = {
            'question': 'Pergunta',
        }

class ProductAnswer(forms.ModelForm):
    class Meta:
        model = models.ProductAnswer
        fields = ['answer']
        widgets = {
            'answer': forms.Textarea(attrs={'class': 'inputs form-control'}),

        }
        labels = {
            'answer': 'Resposta',
        }