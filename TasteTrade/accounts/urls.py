# myapp/urls.py
from django.urls import path
from . import views
from .views import login_view


urlpatterns = [
    path('signup_Bus/', views.signup_Bus, name='signup_Bus'),
    path('signup_Sup/', views.signup_Sup, name='signup_Sup'),
    path('login/', login_view, name='login_view'),

]
