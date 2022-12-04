from django.urls import path
from .views import cart_page, add_product, decrement_product, delete_product, clean_cart
urlpatterns = [
    path('', cart_page, name='cart'),
    path('add/<int:product_id>/',add_product, name='add'),
    path('decrement/<int:product_id>/',decrement_product, name='decrement'),
    path('delete/<int:producto_id>/',delete_product, name='delete'),
    path('clean/',clean_cart, name='clean')
]
