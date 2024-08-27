from django.urls import path
from . import views
from .views import submit_application

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('home/', views.home, name='home'),
    path('meet-the-team/', views.meet_the_team, name='meet_the_team'),
    path('about-us/', views.about_us, name='about_us'),
    path('our-services/', views.our_services, name='our_services'),
    path('our-story/', views.our_story, name='our_story'),
    path('sustainability/', views.sustainability, name='sustainability'),
    path('careers/', views.careers, name='careers'),
    path('faqs/', views.faqs, name='faqs'),
    path('shipping-returns/', views.shipping_returns, name='shipping_returns'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('apply/', submit_application, name='submit_application'),
    path('pricing/', views.pricing, name='pricing_page'),

]
