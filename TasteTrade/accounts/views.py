
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
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



def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Check user credentials
            user = authenticate(request, username=username, password=password)
            if user:
                # Log in the user
                login(request, user)
                messages.success(request, "Logged in successfully", extra_tags="alert-success")
                return redirect(request.GET.get("next", "/"))
            else:
                messages.error(request, "Please try again. Your credentials are wrong", extra_tags="alert-danger")
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
