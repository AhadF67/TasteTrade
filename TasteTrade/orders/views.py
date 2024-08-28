from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Review
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from .forms import ReviewForm
from accounts.models import Profile
from products.models import Product
from django.db.models import Q, Sum
from fpdf import FPDF
from PyPDF2 import PdfWriter, PdfReader
import os

@login_required
def order_list(request):
    user_profile = Profile.objects.get(user=request.user)
    user_type = user_profile.user_type

    # Get the selected status and sort order from the request
    selected_status = request.GET.get('status', '')
    sort_order = request.GET.get('sort', 'desc')  # Default to descending (newest first)

    if user_type == 'sup':
        supplier_products = Product.objects.filter(supplier=request.user)
        orders = Order.objects.filter(product__in=supplier_products)
    else:
        orders = Order.objects.filter(user=request.user)

    # Apply status filter if one is selected
    if selected_status:
        orders = orders.filter(status=selected_status)

    # Apply sorting based on the selected sort order
    if sort_order == 'asc':
        orders = orders.order_by('created_at')
    else:
        orders = orders.order_by('-created_at')

    return render(request, 'orders/order_list.html', {
        'orders': orders,
        'user_type': user_type,
        'selected_status': selected_status,
        'sort_order': sort_order,
    })


from django.db.models import Sum, Q
from django.contrib.auth.decorators import login_required

@login_required
def orders_summary(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    
    if user_profile.user_type == 'sup':
        # If the user is a supplier, filter orders by the products they supply
        supplier_products = Product.objects.filter(supplier=user)
        orders = Order.objects.filter(product__in=supplier_products)
    else:
        # If the user is a regular customer, filter orders by the user
        orders = Order.objects.filter(user=user)
    
    total_paid = orders.aggregate(Sum('total_price'))['total_price__sum'] or 0
    total_orders = orders.count()
    completed_orders = orders.filter(status='completed').count()
    canceled_orders = orders.filter(status='canceled').count()
    pending_orders = orders.filter(status='pending').count()
    approved_orders = orders.filter(status='approved').count()
    rejected_orders = orders.filter(status='rejected').count()
    
    context = {
        'orders': orders,
        'total_paid': total_paid,
        'total_orders': total_orders,
        'completed_orders': completed_orders,
        'canceled_orders': canceled_orders,
        'pending_orders': pending_orders,
        'approved_orders': approved_orders,
        'rejected_orders': rejected_orders,
    }
    
    return render(request, 'orders/orders_summary.html', context)


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
    if order.status == 'pending':
        order.status = 'approved'
        order.save()
        print("Order status updated to Approved")
        confirm_pop(request)
    else:
        print("Order status is not 'pending'")
    return redirect('order_list')


@login_required
def reject_order(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    if order.status == 'pending':
        order.status = 'rejected'
        order.save()
        reject_pop(request)
    return redirect('order_list')




@login_required
def cancel_order(request, order_number):
    
    order = get_object_or_404(Order, order_number=order_number)
    if order.status == 'pending':
        order.status = 'canceled'
        order.save()
        cancel_pop(request)
    return redirect('order_list')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ShippingForm, PaymentForm
from .models import Order
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

            return redirect('order_list')
        else:
            # Print errors if forms are invalid
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
        'order': order,
        'shipping_errors': shipping_form.errors,
        'payment_errors': payment_form.errors,
    })






from django.shortcuts import render, redirect
from .forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactUsForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']

            # Construct the email subject and message
            subject = f"New Contact Us Message from {name}"
            message_body = f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\nMessage: {message}"

            # Send the email
            send_mail(
                subject,
                message_body,
                'BlueHuawei67_@outlook.com',  #from
                ['TasteTrade0@gmail.com'],  #to
                fail_silently=False,
            )

            # Redirect to a success page
            return redirect('send_success')  # Make sure you have a 'success' URL or page defined
    else:
        form = ContactUsForm()
    return render(request, 'orders/contact_us.html', {'form': form})


def success(request):
    return render(request, 'orders/success.html')


from django.shortcuts import render, redirect
from .forms import ShippingForm, PaymentForm



def delete_pop(request):
    return render(request, 'orders/delete_POP.html')

def cancel_pop(request):
    return render(request, 'orders/cancel_POP.html')

def confirm_pop(request):
    return render(request, 'orders/confirm_POP.html')

def reject_pop(request):
    return render(request, 'orders/reject_POP.html')

from django.shortcuts import render


from django.shortcuts import redirect
from django.contrib import messages
from .models import Review

from django.shortcuts import get_object_or_404
from django.db.models import Avg,Min
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
   
    min_rating = reviews.aggregate(Min('rating'))['rating__min']
    
 
    return render(request, 'orders/review_summary.html', {
        'reviews': reviews,
        'average_rating': average_rating,
        'name': supplier_name
    })


from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import Http404

def review_view(request, order_number, name):
    # Fetch the order based on order_number
    order = get_object_or_404(Order, order_number=order_number)
    
    # Fetch profiles based on user_type
    user_type = request.user.profile.user_type
    context = {
        'order_number': order_number,
    }

    if user_type == 'bus':
        try:
            supplier_profile = Profile.objects.get(user=order.product.supplier)
            context['label'] = 'Supplier'
            context['name'] = supplier_profile.name  # Set supplier name as 'name'
        except Profile.DoesNotExist:
            raise Http404("Supplier profile not found.")
        template_name = 'orders/review.html'
        
    elif user_type == 'sup':
        try:
            business_profile = Profile.objects.get(user=order.user)
            context['label'] = 'Business'
            context['name'] = business_profile.name  # Set business name as 'name'
        except Profile.DoesNotExist:
            raise Http404("Business profile not found.")
        template_name = 'orders/review.html'
    
    else:
        raise Http404("User type not recognized.")

    return render(request, template_name, context)



import tempfile


@login_required
def generate_contract_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    try:
        supplier_profile = Profile.objects.get(user=order.product.supplier)
    except Profile.DoesNotExist:
        raise Http404("Supplier profile not found for this product.")

    try:
        business_profile = Profile.objects.get(user=order.user)
    except Profile.DoesNotExist:
        raise Http404("Business profile not found.")

    pdf = FPDF()
    pdf.add_page()
    
    # Add logo
    logo_path = os.path.join('orders/static/images/logo1.png')
    pdf.image(logo_path, x=10, y=8, w=30) 

    pdf.ln(30)

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, f"Contract for Order #{order.order_number}", ln=True, align='C')
    pdf.ln(10)

    # Supplier Information
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(200, 10, "Supplier Information:", ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.cell(200, 10, f"Name: {supplier_profile.name}", ln=True)
    pdf.cell(200, 10, f"Phone Number: {supplier_profile.phone_number}", ln=True)
    pdf.cell(200, 10, f"Rating: {supplier_profile.rating}", ln=True)
    pdf.ln(10)

    # Business Information
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(200, 10, "Business Information:", ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.cell(200, 10, f"Name: {business_profile.name}", ln=True)
    pdf.cell(200, 10, f"Phone Number: {business_profile.phone_number}", ln=True)
    pdf.ln(10)

    # Order Information
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(200, 10, "Order Information:", ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.cell(200, 10, f"Product: {order.product.name}", ln=True)
    pdf.cell(200, 10, f"Quantity: {order.quantity}", ln=True)
    pdf.cell(200, 10, f"Total Price: {order.total_price} SR", ln=True)
    pdf.cell(200, 10, f"Frequency: {order.get_duration_first_display()}", ln=True)
    pdf.cell(200, 10, f"Duration: {order.get_duration_second_display()}", ln=True)
    pdf.ln(10)

    # Terms and Conditions
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(200, 10, "Terms and Conditions:", ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, "1. The product will be delivered according to the selected frequency and duration.\n"
                          "2. The business owner agrees to pay the total amount upon delivery.\n"
                          "3. Any cancellations must be communicated 24 hours before the scheduled delivery.\n")

    # Use tempfile to create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
        pdf_file_path = temp_file.name
        pdf.output(pdf_file_path)
    
    # Read and serve the PDF file
    reader = PdfReader(pdf_file_path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="contract_{order.order_number}.pdf"'
    writer.write(response)
    
    # Clean up the temporary file
    os.remove(pdf_file_path)
    
    return response
