from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.shortcuts import render

def main_home(request: HttpRequest):
    return render(request, 'main/main_home.html')

def second_home(request: HttpRequest):
    return render(request, 'main/home_bus.html')

def third_home(request: HttpRequest):
    return render(request, 'main/home_sup.html')

