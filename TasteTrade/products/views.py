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
#@user_passes_test(is_supplier)
def supplier_dashboard(request):
    products = Product.objects.filter(supplier=request.user)
    # Debugging: print the number of products
    print(f"Number of products: {products.count()}")  
    return render(request, 'supplier_dashboard.html', {'products': products})

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

def order_product(request: HttpRequest, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.user = request.user
            order.total_price = order.quantity * product.price  
            order.order_number = get_random_string(length=10)  
            order.save()
            return redirect('success')

    else:
        form = OrderForm()
    initial_total = product.price
    return render(request, 'order_product.html', {'product': product, 'form': form, 'initial_total': initial_total})
