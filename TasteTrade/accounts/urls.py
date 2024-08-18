# myapp/urls.py
from django.urls import path
from . import views
from .views import login_view


urlpatterns = [
    path('signup_Bus/', views.signup_Bus, name='signup_Bus'),
    path('signup_Sup/', views.signup_Sup, name='signup_Sup'),
    path('login/',  views.login_view, name='login_view'),
    path('profile/<int:profile_id>/', views. profile_view, name='profile_view'),


]
