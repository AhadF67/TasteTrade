# forms.py
from django import forms

class LoginForm_admin(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
