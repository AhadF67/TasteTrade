from django import forms
from .models import Product, Order


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
    class Meta:
        model = Order
        fields = ['quantity', 'category', 'description', 'expiry_date']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1, 'max': 100, 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        total = forms.DecimalField(label="Total", disabled=True, required=False)

        def save(self, commit=True):
            order = super().save(commit=False)
            order.total_price = order.quantity * order.product.price
            if commit:
                order.save()
            return order
