from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Review
from .forms import ReviewForm
from accounts.models import Profile
from products.models import Product

from django.db.models import Q

@login_required
def order_list(request):
    user_profile = Profile.objects.get(user=request.user)
    user_type = user_profile.user_type

    # Get the selected status from the request
    selected_status = request.GET.get('status', '')

    if user_type == 'sup':
        # Get the products that belong to the supplier
        supplier_products = Product.objects.filter(supplier=request.user)
        # Filter orders based on these products
        orders = Order.objects.filter(product__in=supplier_products)
    else:
        # If the user is a business owner, show their own orders
        orders = Order.objects.filter(user=request.user)

    # Apply status filter if one is selected
    if selected_status:
        orders = orders.filter(status=selected_status)

    return render(request, 'orders/order_list.html', {
        'orders': orders,
        'user_type': user_type,
        'selected_status': selected_status,
    })


from django.shortcuts import redirect, get_object_or_404
from .models import Order



from django.shortcuts import redirect, get_object_or_404
from .models import Order
from django.contrib.auth.decorators import login_required

@login_required
def confirm_order(request, order_number):
    print("Order number:", order_number)
    order = get_object_or_404(Order, order_number=order_number)
    print("Order found:", order)
    if order.status == 'in_progress':
        order.status = 'confirmed'
        order.save()
        print("Order status updated to confirmed")
        confirm_pop(request)
    else:
        print("Order status is not 'in_progress'")
    return redirect('order_list')


@login_required
def reject_order(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    if order.status == 'in_progress':
        order.status = 'rejected'
        order.save()
        reject_pop(request)
    return redirect('order_list')




@login_required
def cancel_order(request, order_number):
    
    order = get_object_or_404(Order, order_number=order_number)
    if order.status == 'in_progress':
        order.status = 'canceled'
        order.save()
        cancel_pop(request)
    return redirect('order_list')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ShippingForm, PaymentForm
from .models import Order
@login_required
def checkout_order(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    
    if request.method == 'POST':
        shipping_form = ShippingForm(request.POST, prefix='shipping')
        payment_form = PaymentForm(request.POST, prefix='payment')
        
        if shipping_form.is_valid() and payment_form.is_valid():
            # Debug: Check if forms are valid and data is being processed
            print("Forms are valid. Processing the data...")

            # Process shipping form data
            shipping_data = shipping_form.cleaned_data
            order.shipping_address = shipping_data.get('address')
            order.first_name = shipping_data.get('first_name')
            order.last_name = shipping_data.get('last_name')
            order.email = shipping_data.get('email')
            order.phone_number = shipping_data.get('phone_number')
            
            # Process payment form data
            payment_data = payment_form.cleaned_data
            order.name_on_card = payment_data.get('name_on_card')
            order.card_number = payment_data.get('card_number')
            order.expiry_date = payment_data.get('expiry_date')
            order.cvv = payment_data.get('cvv')
            
            # Update the order status
            order.status = 'completed'
            order.save()

            # Debug: Check if order status is being updated
            print(f"Order status updated to: {order.status}")

            # Redirect to the order list page
            return redirect('order_list')
        else:
            # Debug: Check which form is invalid
            print("Invalid form data")
            print(shipping_form.errors)
            print(payment_form.errors)
    else:
        shipping_form = ShippingForm(prefix='shipping')
        payment_form = PaymentForm(prefix='payment')
    
    return render(request, 'orders/checkout.html', {
        'shipping_form': shipping_form,
        'payment_form': payment_form,
        'order_number': order_number, 
        'order': order
    })





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

from django.shortcuts import render

#def review_sup_pop(request, order_number, supplier_name):
    #return render(request, 'orders/review_sup.html', {
        #'order_number': order_number,
        #'supplier_name': supplier_name
    #})


#def review_bus_pop(request):
    #return render(request, 'orders/review_bus.html')

from django.shortcuts import redirect
from django.contrib import messages
from .models import Review

from django.shortcuts import get_object_or_404
from django.db.models import Avg
from .models import Review
from accounts.models import Profile

from django.core.exceptions import ValidationError

from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Review

def submit_rating(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your rating has been successfully submitted.')
            return redirect('success')
        else:
            messages.error(request, 'There was an error with your submission.')
            return redirect('review_view', order_number=request.POST.get('order_number'), name=request.POST.get('supplier_name'))
    return redirect('home')

@login_required
def review_order(request, order_id):
    # Implement your review logic here
    return redirect('order_list')


def review_summary(request, supplier_name):
    reviews = Review.objects.filter(supplier_name=supplier_name)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'orders/review_summary.html', {
        'reviews': reviews,
        'average_rating': average_rating,
        'name': supplier_name
    })


from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import Http404
def review_view(request, order_number, name):
    if not name:
        raise Http404("Order name is missing.")
    user_type = request.user.profile.user_type
    context = {
        'order_number': order_number,
        'name': name
    }

    if user_type == 'sup':
        template_name = 'orders/review.html'
        context['label'] = 'Supplier:'
    elif user_type == 'bus':
        template_name = 'orders/review.html'
        context['label'] = 'Business:'
    else:
        raise Http404("User type not recognized.")

    return render(request, template_name, context)
