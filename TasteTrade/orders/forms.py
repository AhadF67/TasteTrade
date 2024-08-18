from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Message...', widget=forms.Textarea(attrs={'class': 'form-control'}))
