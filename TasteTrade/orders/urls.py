from django.urls import path
from . import views
urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('<int:order_id>/delete/', views.delete_order, name='delete_order'),
    path('<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
    path('<int:order_id>/checkout/', views.checkout_order, name='checkout_order'),
    path('<int:order_id>/review/', views.review_order, name='review_order'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('success/', views.success, name='success'),
    path('shipping-details/', views.shipping_details, name='shipping_details'),
    path('payment-details/', views.payment_details, name='payment_details'),

    path('delete-pop/', views.delete_pop, name='delete_pop'),
    path('reject-pop/', views.reject_pop, name='reject_pop'),
    path('cancel-pop/', views.cancel_pop, name='cancel_pop'),
    path('confirm-pop/', views.confirm_pop, name='confirm_pop'),

    path('review-sup/', views.review_sup_pop, name='review_sup'),
    path('review-bus/', views.review_bus_pop, name='review_bus'),



    path('submit_rating/', views.submit_rating, name='submit_rating'),
    path('review_summary/', views.review_summary, name='review_summary'),

]

