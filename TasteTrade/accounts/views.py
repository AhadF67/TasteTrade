
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import UserForm
from .forms import SupplierSignUpForm
from .models import Profile
import logging

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


logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            logger.debug(f"Attempting to authenticate user with username: {username}")
            user = authenticate(request, username=username, password=password)
            print(user, username, password)

            if user is not None:
                login(request, user)
                return redirect('success')  
            else:
                form.add_error(None, 'Invalid username or password')
                logger.debug('Authentication failed')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

def profile_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, 'accounts/profile_Sup.html', {'profile': profile})

def signup_pop(request):
    return render(request, 'accounts/signup_options.html')

def forget_pop(request):
    return render(request, 'accounts/forget_pop.html')
