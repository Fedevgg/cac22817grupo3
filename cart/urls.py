from django.urls import path
from . import views
cart_patterns = [
    path('', views.cart_page, name='cart'),
    path('add/<int:product_id>/', views.add_product, name='add'),
    path('decrement/<int:product_id>/', views.decrement_product, name='decrement'),
    path('delete/<int:product_id>/', views.delete_product, name='delete'),
    path('clean/',views.clean_cart, name='clean')
]
