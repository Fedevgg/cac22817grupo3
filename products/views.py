from django.http import HttpResponseRedirect
from django.urls import reverse
from cart.models import CartItem
from .models import Product
from django.views.generic import ListView, DetailView
# Create your views here.

class CatalogView(ListView):
    model = Product
    
class ItemView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

def agregar_item_carrito(request, target):
    print(target)
    print(type(target))
    try:
        busqueda_item = CartItem.objects.get(user=request.user, product_id=target, confirmado=False)
    except CartItem.DoesNotExist:
        busqueda_item = None
    if not busqueda_item:
        item = CartItem(
            product_id_id=target,
            user=request.user,
            cantidad=1,
            confirmado=False,
        )
        item.save()
    else:
        busqueda_item.cantidad += 1
        busqueda_item.save()
    
    return HttpResponseRedirect(reverse('catalog:catalog'))
    
