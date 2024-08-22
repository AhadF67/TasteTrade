from django.shortcuts import render,  get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, OrderForm
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def is_supplier(user):
    return user.is_authenticated and hasattr(user, 'is_supplier') and user.is_supplier


@login_required
#@user_passes_test(is_supplier)
def supplier_dashboard(request):
    products = Product.objects.filter(supplier=request.user)
    return render(request, 'supplier_dashboard.html', {'products': products})

@login_required
#@user_passes_test(is_supplier)
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.supplier = request.user  # Set the supplier field
            product.save()
            return redirect('supplier_dashboard')  # Redirect to dashboard after saving
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})


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
    return render(request, 'delete_product.html', {'product': product})


from django.utils.crypto import get_random_string

def order_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.user = request.user
            order.total_price = order.quantity * product.price  # Calculate total price
            order.order_number = get_random_string(length=10)  # Generate unique order number
            order.save()
            return redirect('confirm_order')
    else:
        form = OrderForm()
    initial_total = product.price
    return render(request, 'order_product.html', {'product': product, 'form': form, 'initial_total': initial_total})
