from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('products/', views.product_list, name='product_list'),
    path('dashboard/', views.supplier_dashboard, name='supplier_dashboard'),
    path('order/<int:product_id>/', views.order_product, name='order_product'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
