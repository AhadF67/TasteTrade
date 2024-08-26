from django.urls import path
from . import views
urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('order/<str:order_number>/confirm/', views.confirm_order, name='confirm_order'),
    path('order/<str:order_number>/reject/', views.reject_order, name='reject_order'),
    path('order/<str:order_number>/cancel/', views.cancel_order, name='cancel_order'),
    
    path('order/<str:order_number>/checkout/', views.checkout_order, name='checkout_order'),
    
    #path('order/<int:order_id>/review/', views.review_order, name='review_order'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('success/', views.success, name='success'),
    path('shipping-details/', views.shipping_details, name='shipping_details'),
    path('payment-details/', views.payment_details, name='payment_details'),

    path('delete-pop/', views.delete_pop, name='delete_pop'),
    path('reject-pop/', views.reject_pop, name='reject_pop'),
    path('cancel-pop/', views.cancel_pop, name='cancel_pop'),
    path('confirm-pop/', views.confirm_pop, name='confirm_pop'),
    
    path('review/<str:order_number>/<str:name>/', views.review_view, name='review_view'),

    path('review-summary/<str:supplier_name>/', views.review_summary, name='review_summary'),

    #path('review-sup/<int:order_number>/<str:supplier_name>/', views.review_sup_pop, name='review_sup'),
    
    #path('review-bus/', views.review_bus_pop, name='review_bus'),

    path('orders_summary/', views.orders_summary, name='orders_summary'),

    path('submit_rating/', views.submit_rating, name='submit_rating'),
    
    path('generate_contract/<int:order_id>/', views.generate_contract_pdf, name='generate_contract'),

]

