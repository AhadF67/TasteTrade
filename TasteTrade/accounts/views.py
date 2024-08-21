
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserForm
from .models import Profile
from .forms import UserForm
from django.contrib import messages
from django.conf import settings

import logging

def signup_Bus(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                profile = Profile.objects.create(user=user, name=user.username, user_type='bus')
                logging.info(f"Profile created for user {user.username} with ID {profile.id}")
                return redirect('success')
            except Exception as e:
                logging.error(f"Error creating profile for user {user.username}: {str(e)}")
                messages.error(request, "There was an error creating your profile. Please try again.")
        else:
            logging.warning("Form is not valid.")
    else:
        form = UserForm()
    return render(request, 'accounts/signup_Bus.html', {'form': form})


def signup_Sup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user, name=user.username, user_type='sup')
            return redirect('success')
    else:
        form = UserForm()
    return render(request, 'accounts/signup_Sup.html', {'form': form})


def login_view(request: HttpRequest):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # Get user profile
                profile = Profile.objects.get(user=user)
                if profile.user_type == 'sup':
                    return redirect('home_sup')  
                elif profile.user_type == 'bus':
                    return redirect('home_bus') 
                else:
                    return redirect('main_home') 
            else:
                messages.error(request, "Invalid credentials. Please try again.", extra_tags="alert-danger")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})



def profile_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if profile.image:
        image_url = profile.image.url
    else:

        image_url = '\media\images\default.jpg'  # Path to a default image if none exists

    return render(request, 'accounts/profile_Sup.html', {'profile': profile, 'image_url': image_url})


    return render(request, 'accounts/profile_Sup.html', {'profile': profile, 'images_url': image_url})

def signup_pop(request):
    return render(request, 'accounts/signup_options.html')

def forget_pop(request):
    return render(request, 'accounts/forget_pop.html')

def logout_pop(request):
    return render(request, 'accounts/logout_pop.html')
