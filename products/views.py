from .models import Product
from django.views.generic import ListView, DetailView
# Create your views here.

class CatalogView(ListView):
    model = Product
    
class ItemView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
