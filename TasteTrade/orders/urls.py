from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('<int:order_id>/delete/', views.delete_order, name='delete_order'),
    path('<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
    path('<int:order_id>/checkout/', views.checkout_order, name='checkout_order'),
    path('<int:order_id>/review/', views.review_order, name='review_order'),
    path('contact-us/', views.contact_us, name='contact_us'),
]
