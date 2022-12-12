from django.urls import path
from .views import CatalogView, ItemView, agregar_item_carrito

catalog_patterns = ([
    path('', CatalogView.as_view(), name='catalog'),
    path('item/<int:pk>/<slug:name>', ItemView.as_view(), name='product'),
    path('add_item/<int:target>', agregar_item_carrito, name='agregar'),
], 'catalog')
