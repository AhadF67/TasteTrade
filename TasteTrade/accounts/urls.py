# myapp/urls.py
from django.urls import path
from . import views
from .views import login_view


urlpatterns = [
    path('register/', views.register, name='register'),
    path('sign_up/', views.signup, name='signup'),
    path('login/', login_view, name='login_view'),


]
