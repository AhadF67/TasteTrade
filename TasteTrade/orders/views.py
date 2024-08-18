from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from django.contrib.auth.decorators import login_required


@login_required
def order_list(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Replace 'login' with your login URL or view name
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.delete()
    return redirect('order_list')

def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.status = 'cancelled'  # Assuming 'cancelled' is a valid status you add
    order.save()
    return redirect('order_list')

def checkout_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    # Implement checkout logic here
    return redirect('order_list')

def review_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    # Implement review logic here
    return redirect('order_list')

from django.shortcuts import render, redirect
from .forms import ContactUsForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email)
            return redirect('success')  # Redirect to a success page or any other page
    else:
        form = ContactUsForm()
    return render(request, 'contact_us.html', {'form': form})
