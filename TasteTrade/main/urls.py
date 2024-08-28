from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home, name='main_home'),
    path('home/', views.home, name='home'),
    path('meet-the-team/', views.meet_the_team, name='meet_the_team'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('activate-supplier/<int:profile_id>/', views.activate_supplier, name='activate_supplier'),
    path('toggle_activation/<int:profile_id>/', views.toggle_activation, name='toggle_activation'),

]