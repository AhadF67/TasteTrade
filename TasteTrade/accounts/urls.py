# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('signup_Bus/', views.signup_Bus, name='signup_Bus'),
    path('signup_Sup/', views.signup_Sup, name='signup_Sup'),
    path('login/',  views.login_view, name='login_view'),
    path('profile/<int:profile_id>/', views. profile_view, name='profile_view'),

    path('profile/edit/', views.update_profile, name='edit_profile'),

    path('logout-pop/', views.logout_pop, name='logout_pop'),
    path('signup-pop/', views.signup_pop, name='signup_pop'),
    

    path('forget-pop/', views.forget_pop, name='forget_pop'),
    
    path('password-reset/', views.password_reset_request, name='password_reset_request'),
    path('password-reset-done/', TemplateView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),

    
    
    path('statics/', views.supplier_statistics, name='supplier_statistics'),
    
    
    path('profile/pdf/', views.order_list_for_pdf, name='order_list_for_pdf'),
    
]

