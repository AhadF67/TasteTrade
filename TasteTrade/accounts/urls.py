# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup_Bus/', views.signup_Bus, name='signup_Bus'),
    path('signup_Sup/', views.signup_Sup, name='signup_Sup'),
    path('login/',  views.login_view, name='login_view'),
    path('profile/<int:profile_id>/', views. profile_view, name='profile_view'),

    path('profile/edit/', views.update_profile, name='edit_profile'),

    path('signup-pop/', views.signup_pop, name='signup_pop'),
    path('forget-pop/', views.forget_pop, name='forget_pop'),
    
    path('logout-pop/', views.logout_pop, name='logout_pop'),
    
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('statics/', views.supplier_statistics, name='supplier_statistics'),
    path('profile/pdf/', views.order_list_for_pdf, name='order_list_for_pdf'),
    
]

