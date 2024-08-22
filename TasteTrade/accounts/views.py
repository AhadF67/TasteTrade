
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile
from .forms import UserForm
from django.contrib import messages
from django.conf import settings
from django.templatetags.static import static
from django.contrib.auth.decorators import login_required, user_passes_test



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



from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.templatetags.static import static

def profile_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    
    # Determine the image URL
    if profile.image:
        image_url = profile.image.url
    else:
        image_url = static('images/default.jpg')

    # Determine if the "Statistics" button should be shown
    show_statistics_button = profile.user.profile.user_type == 'sup'

    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'image_url': image_url,
        'show_statistics_button': show_statistics_button
    })





def signup_pop(request):
    return render(request, 'accounts/signup_options.html')

def forget_pop(request):
    return render(request, 'accounts/forget_pop.html')

def logout_pop(request):
    return render(request, 'accounts/logout_pop.html')



# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get('password')

            if password:
                user.set_password(password)
            user.save()
            profile_form.save()

            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile_view', profile_id=request.user.profile.id) 
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/edit_profile.html', context)
