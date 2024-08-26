from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('home/', views.home, name='home'),
    path('meet-the-team/', views.meet_the_team, name='meet_the_team'),
]