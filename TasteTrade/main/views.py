from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.shortcuts import render

def main_home(request: HttpRequest):
    context = {'home_type': 'main'}
    return render(request, 'main/main_home.html', context)

def second_home(request: HttpRequest):
    context = {'home_type': 'business'}
    return render(request, 'main/home_bus.html', context)

def third_home(request: HttpRequest):
    context = {'home_type': 'supplier'}
    return render(request, 'main/home_sup.html', context)