from django import forms
from .models import Product
from orders.models import Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'category', 'description', 'expiry_date', 'image']


        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'expiry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }


class OrderForm(forms.ModelForm):
    DURATION_CHOICES_FIRST = [
        ('once_a_week', 'Once a Week'),
        ('twice_a_week', 'Twice a Week'),
    ]

    DURATION_CHOICES_SECOND = [
        ('one_month', 'One Month'),
        ('two_months', 'Two Months'),
        ('three_months', 'Three Months'),
    ]

    duration_first = forms.ChoiceField(
        choices=DURATION_CHOICES_FIRST,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Select Frequency"
    )
    duration_second = forms.ChoiceField(
        choices=DURATION_CHOICES_SECOND,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Select Duration"
    )

    class Meta:
        model = Order
        fields = ['quantity', 'expiry_date', 'duration_first', 'duration_second']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1, 'max': 100, 'class': 'form-control'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }