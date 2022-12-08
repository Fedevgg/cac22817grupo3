from django.urls import path, include
from . import views


core_patterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('cart/', include('cart.urls'), name='cart')
]