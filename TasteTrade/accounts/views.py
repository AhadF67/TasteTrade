
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import UserForm
from .forms import SupplierSignUpForm

def signup_Bus(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or login page
    else:
        form = UserForm()

    return render(request, 'accounts/signup_Bus.html', {'form': form})


# views.py


def signup_Sup (request):
    if request.method == 'POST':
        form = SupplierSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle form processing, save files, etc.
            # Save the form data or create a new Supplier model instance
            pass
    else:
        form = SupplierSignUpForm()

    return render(request, 'accounts/signup_Sup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home or any other page after login
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})
