from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

core_patterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('cart/', include('cart.urls'), name='cart'),
    path('registrarse/', views.core_registrarse, name='registrarse'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.core_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/index.html'), name='logout'),
    path('compras/', views.compras, name='compras')
]