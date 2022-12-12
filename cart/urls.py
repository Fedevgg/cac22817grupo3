from django.urls import path
from . import views
cart_patterns = [
    path('', views.cart_view, name='cart'),
    path('add_item/<int:target>', views.agregar_item_carrito, name='agregar'),
    path('subs_item/<int:target>', views.restar_item_carrito, name='restar'),
    path('del_item/<int:target>', views.borrar_item_carrito, name='borrar'),
    path('clean/', views.limpiar_carrito, name='limpiar'),
    path('send/', views.confirmar_carrito, name='confirmar'),
]
