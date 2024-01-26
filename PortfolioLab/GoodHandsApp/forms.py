import datetime

from django import forms
from django.core.validators import EmailValidator


class LoginForm(forms.Form):
    email = forms.CharField(max_length=64, label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Hasło')
