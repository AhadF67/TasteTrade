from django.shortcuts import render,  get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, OrderForm, CategoryForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.crypto import get_random_string

from django.http import HttpRequest


# Create your views here.

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    keywords = request.GET.get('keywords')
    selected_categories = request.GET.getlist('category')
    max_price = request.GET.get('price')

    if keywords:
        products = products.filter(name__icontains=keywords) | products.filter(description__icontains=keywords)
    if selected_categories:
        products = products.filter(category__id__in=selected_categories)
    if max_price:
        products = products.filter(price__lte=max_price)

    context = {
        'products': products,
        'categories': categories,
        'selected_categories': selected_categories,
        'keywords': keywords,
        'max_price': max_price if max_price else 50,
    }
    return render(request, 'product_list.html', context)


def is_supplier(user):
    return user.is_authenticated and hasattr(user, 'is_supplier') and user.is_supplier


@login_required
def supplier_dashboard(request):
    query = request.GET.get('q')  # Get the search query from the request
    products = Product.objects.filter(supplier=request.user)
    
    # Apply the search filter if there is a query
    if query:
        products = products.filter(name__icontains=query)
    
    return render(request, 'supplier_dashboard.html', {'products': products, 'query': query})


@login_required
#@user_passes_test(is_supplier)
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category') 
    else:
        form = CategoryForm()
    
    categories = Category.objects.all()
    return render(request, 'add_category.html', {'form': form})

@login_required
#@user_passes_test(is_supplier)
def add_product(request):
    categories = Category.objects.all()
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.supplier = request.user
            product.save()
            return redirect('supplier_dashboard')
        else:
            print(form.errors)  # Debug form errors
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form, 'categories': categories})


@login_required
#@user_passes_test(is_supplier)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, supplier=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('supplier_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})

@login_required
#@user_passes_test(is_supplier)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, supplier=request.user)
    if request.method == 'POST':
        product.delete()
        return redirect('supplier_dashboard')
    return render(request, 'delete_products.html', {'product': product})

DURATION_MULTIPLIERS_FIRST = {
    'once_a_week': 1,
    'twice_a_week': 2,
}

DURATION_MULTIPLIERS_SECOND = {
    'one_month': 4,   # Assuming 4 weeks in a month
    'two_months': 8,
    'three_months': 12,
}

from datetime import date

def order_product(request: HttpRequest, product_id):
    product = get_object_or_404(Product, id=product_id)
    is_expired = product.expiry_date < date.today()
    
    if is_expired:
        message = "This product has expired and cannot be ordered."
    else:
        message = None
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid() and not is_expired:
            order = form.save(commit=False)
            order.product = product
            order.user = request.user
            
            duration_first = form.cleaned_data['duration_first']
            duration_second = form.cleaned_data['duration_second']
            multiplier_first = DURATION_MULTIPLIERS_FIRST[duration_first]
            multiplier_second = DURATION_MULTIPLIERS_SECOND[duration_second]
            
            total = order.quantity * product.price * multiplier_first * multiplier_second
            
            if order.quantity > product.quantity:
                message = "Ordered quantity exceeds available product quantity."
            else:
                order.total_price = total
                product.quantity -= order.quantity  # Subtract ordered quantity from product stock
                product.save()
                order.order_number = get_random_string(length=5)
                order.save()
                return redirect('success')
    else:
        form = OrderForm()
    
    initial_total = product.price
    return render(request, 'order_product.html', {
        'product': product,
        'form': form,
        'initial_total': initial_total,
        'is_expired': is_expired,
        'message': message,
    })

