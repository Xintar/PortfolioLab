from django import forms
from django.forms import ModelForm

from GoodHandsApp.models import User


class LoginForm(forms.Form):
    email = forms.CharField(max_length=64, label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Hasło')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']
