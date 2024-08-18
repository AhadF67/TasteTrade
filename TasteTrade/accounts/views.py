
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import UserForm
from .forms import SupplierSignUpForm
from .models import Profile


def signup_Bus(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') 
    else:
        form = UserForm()

    return render(request, 'accounts/signup_Bus.html', {'form': form})


def signup_Sup (request):
    if request.method == 'POST':
        form = SupplierSignUpForm(request.POST, request.FILES)
        if form.is_valid():
      
            pass
    else:
        form = SupplierSignUpForm()

    return render(request, 'accounts/signup_Sup.html', {'form': form})

import logging
logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            logger.debug(f"Attempting to authenticate user with email: {email}")
            user = authenticate(request, username=email, password=password)
            print(user,email,password)

            print('success')
            if user is not None:
                login(request, user)
                return redirect('success')
            else:
                form.add_error(None, 'Invalid email or password')
                logger.debug('Authentication failed')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})



def profile_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, 'accounts/profile_Sup.html', {'profile': profile})
