# myapp/forms.py
from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django.core.validators import RegexValidator


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password and re_password and password != re_password:
            self.add_error('re_password', "Passwords do not match.")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

class ProfileUpdateForm(forms.ModelForm):
    class Meta:

     model = Profile
     fields = ['name', 'image', 'phone_number']  



class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False, label="New Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput(), required=False, label="Confirm New Password")


    class Meta:
        model = User
        fields = ['email']  # Only email is editable from here

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password or password_confirm:
            if password != password_confirm:
                self.add_error('password_confirm', "Passwords do not match.")
