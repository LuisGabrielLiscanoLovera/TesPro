from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

STATES = (
  
    ('1', 'Despacho'),
    ('2', 'Prod'),
    ('3', 'Acum'),
    ('4', 'Casino')
)

class LoginForm(forms.Form):
  

    username  = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': ' Usuario'}))
    password  = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Clave'}))
    perfilPatinador = forms.ChoiceField(required = False,widget=forms.RadioSelect, choices=STATES)


class RegistrationForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'firstname', 'placeholder': 'clave de usuario'}))
    lastname  = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'lastname', 'placeholder': 'Nombre completo'}))
    email     = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'email', 'name': 'email', 'placeholder': 'Correo electronico'}))
    username  = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Usuario'}))
    password  = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Ingresa clave'}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'confirm-password', 'placeholder': 'Repita clave'}))