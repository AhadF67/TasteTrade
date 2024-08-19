from django.shortcuts import render

from django.shortcuts import render

def main_home(request):
    return render(request, 'main/main_home.html')

def second_home(request):
    return render(request, 'main/home_bus.html')

def third_home(request):
    return render(request, 'main/home_sup.html')

