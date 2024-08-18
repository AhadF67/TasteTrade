from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def order_list(request):
    if not request.user.is_authenticated:
        return redirect('login_view')  # Replace 'login' with your login URL or view name
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
    return render(request, 'orders/contact_us.html', {'form': form})

def success(request):
    return render(request, 'orders/success.html')


from django.shortcuts import render, redirect
from .forms import ShippingForm, PaymentForm

def shipping_details(request):
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            return redirect('payment_details')  # Redirect to payment details modal
    else:
        form = ShippingForm()
    return render(request, 'orders/shipping_details.html', {'form': form})

def payment_details(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            return redirect('success')  # Redirect to success page
    else:
        form = PaymentForm()
    return render(request, 'orders/payment_details.html', {'form': form})

def delete_pop(request):
    return render(request, 'orders/delete_POP.html')

def cancel_pop(request):
    return render(request, 'orders/cancel_POP.html')

def confirm_pop(request):
    return render(request, 'orders/confirm_POP.html')

def reject_pop(request):
    return render(request, 'orders/reject_POP.html')

def review_sup_pop(request):
    return render(request, 'orders/review_sup.html')

def review_bus_pop(request):
    return render(request, 'orders/review_bus.html')

def submit_rating(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        # saving here
        return redirect('success')  
    
    return HttpResponse("Invalid request method.", status=405)


