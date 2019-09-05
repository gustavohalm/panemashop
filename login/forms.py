from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs=dict( required=True, max_length=30, placeholder='silvajose')), label='Usuário' )
    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder='José')), label='Nome')
    last_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder='Silva')), label='Sobrenome')
    email = forms.EmailField(widget=forms.EmailInput( attrs=dict( required=True, max_length=256, placeholder='jose1.silva@email.com' ) ) )
    password = forms.CharField(widget=forms.PasswordInput( attrs=dict( required=True, max_length=30, placeholder='********'))  , label='Sua Senha') 
    password_2 = forms.CharField(widget=forms.PasswordInput( attrs=dict( required=True, max_length=30, placeholder='********')) , label='Repita sua Senha') 
    
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder='silvajose')), label='Usuário')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, placeholder='********')), label='Sua Senha')