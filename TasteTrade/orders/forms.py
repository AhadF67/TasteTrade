from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Message...', widget=forms.Textarea(attrs={'class': 'form-control'}))
    
class ShippingForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', widget=forms.Textarea(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))

class PaymentForm(forms.Form):
    name_on_card = forms.CharField(label='Name on Card', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    card_number = forms.CharField(label='Card Number', max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    expiry_date = forms.CharField(label='Expiry Date (MM/YY)', max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cvv = forms.CharField(label='CVV', max_length=3, widget=forms.TextInput(attrs={'class': 'form-control'}))

