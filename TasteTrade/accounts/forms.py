# myapp/forms.py
from django import forms
from .models import User
from django import forms

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    re_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username','name', 'number', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password and re_password and password != re_password:
            self.add_error('re_password', "Passwords do not match.")



class SupplierSignUpForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    name = forms.CharField(max_length=100)
    number = forms.CharField(max_length=15)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    re_password = forms.CharField(widget=forms.PasswordInput())
    cr = forms.FileField(label='CR')  
    location = forms.CharField(max_length=255)
    bank_account = forms.FileField(label='Bank account')  




class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
