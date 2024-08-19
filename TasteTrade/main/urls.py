from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('home-bus/', views.second_home, name='home_bus'),
    path('home-sup/', views.third_home, name='home_sup'),
]
