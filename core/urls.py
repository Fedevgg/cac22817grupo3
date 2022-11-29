from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


core_patterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
        path('registrarse/', views.core_registrarse, name='registrarse'),
    path('login/', views.core_login, name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='cac/index.html'), name='logout'),
    path('compras/', views.compras,
         name='compras')
]