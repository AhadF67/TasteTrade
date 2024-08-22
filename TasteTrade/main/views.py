from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.shortcuts import render

def main_home(request: HttpRequest):
    context = {'home_type': 'main'}
    return render(request, 'main/main_home.html', context)

def home(request: HttpRequest):
    # Ensure the user is authenticated
    if request.user.is_authenticated:
        user_type = request.user.profile.user_type
    else:
        user_type = None
    
    context = {'user_type': user_type}
    return render(request, 'main/home.html', context)
