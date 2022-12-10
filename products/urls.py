from django.urls import path
from .views import CatalogView, ItemView


catalog_patterns = ([
    path('', CatalogView.as_view(), name='catalog'),
    path('item/<int:pk>/<slug:name>', ItemView.as_view(), name='product'),
], 'catalog')
