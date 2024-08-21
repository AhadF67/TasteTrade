from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Review
from .forms import ReviewForm

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    user_profile = Profile.objects.get(user=request.user)
    user_type = user_profile.user_type  # Assuming 'user_type' is a field in the Profile model
    return render(request, 'orders/order_list.html', {'orders': orders, 'user_type': user_type})

from django.shortcuts import redirect, get_object_or_404
from .models import Order

@login_required
def reject_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status == 'in_progress':
        order.status = 'rejected'
        order.save()
    return redirect('order_list')

@login_required
def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status == 'in_progress':
        order.status = 'confirmed'
        order.save()
    return redirect('order_list')

@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status == 'in_progress':
        order.status = 'canceled'
        order.save()
    return redirect('order_list')

@login_required
def checkout_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status == 'confirmed':
        # Implement your checkout logic here
        order.status = 'completed'
        order.save()
    return redirect('order_list')

@login_required
def review_order(request, order_id):
    # Implement your review logic here
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

from django.shortcuts import redirect
from django.contrib import messages
from .models import Review

def submit_rating(request):
    if request.method == 'POST':
        order_number = request.POST.get('order_number')
        supplier_name = request.POST.get('supplier_name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        # Ensure rating is not None and convert it to integer safely
        try:
            rating = int(rating) if rating else 0
        except ValueError:
            rating = 0

        # Save the review
        Review.objects.create(
            order_number=order_number,
            supplier_name=supplier_name,
            rating=rating,
            comment=comment
        )

        messages.success(request, 'Your rating has been successfully submitted.')
        return redirect('review_summary')

    return redirect('home') 


def review_summary(request):
    reviews = Review.objects.all()
    return render(request, 'orders/review_summary.html', {'reviews': reviews})
