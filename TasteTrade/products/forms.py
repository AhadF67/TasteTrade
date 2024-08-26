from django import forms
from .models import Product, Category
from orders.models import Order


from django import forms
from .models import Product
from orders.models import Order

class ProductForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Desserts', 'Desserts'),
        ('Coffee', 'Coffee'),
        ('Baked Goods', 'Baked Goods'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(), required=True)

    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'category', 'description', 'expiry_date', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter product name'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter price'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Enter quantity'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter product description'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
            'image': forms.ClearableFileInput(),
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
        fields = ['quantity', 'duration_first', 'duration_second']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1, 'max': 100, 'class': 'form-control'}),
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'})
        }