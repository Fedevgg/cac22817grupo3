from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from cart.models import CartItem, PedidoConfirmado
from .forms import CartForm

#class CartView(CreateView):
#    template_name = 'cart/cart.html'
#    # form_class = CartForm
#    model = CartItem
#    fields = ['cantidad']

def cart_view(request):
    items = CartItem.objects.filter(user=request.user, confirmado=False)
    
    data = {
        'added_items': items, # Lista de items
        'form': CartForm()
    }

    if request.method == 'POST':
        form = CartForm(data=request.POST)
        if form.is_valid():
            form.save()
            data['message'] = "Carrito guardado"
        else:
            data['form'] = form

    return render(request, 'cart/cart.html', data)

def agregar_item_carrito(request, target):
    print(target)
    try:
        busqueda_item = CartItem.objects.get(user=request.user, product_id_id=target)
    except CartItem.DoesNotExist:
        busqueda_item = None
    if not busqueda_item:
        item = CartItem(
            product_id_id=target,
            user=request.user,
            cantidad=1,
        )
        item.save()
    else:
        busqueda_item.cantidad += 1
        busqueda_item.save()
    
    return HttpResponseRedirect(reverse('cart'))

def restar_item_carrito(request, target):
    try:
        busqueda_item = CartItem.objects.get(user=request.user, product_id=target)
    except CartItem.DoesNotExist:
        busqueda_item = None
    if busqueda_item:
        if busqueda_item.cantidad > 1:     
            busqueda_item.cantidad -= 1
            busqueda_item.save()
        elif busqueda_item.cantidad == 1:
            busqueda_item.cantidad -= 1
            busqueda_item.delete()
    
    return HttpResponseRedirect(reverse('cart'))

def borrar_item_carrito(request, target):
    try:
        busqueda_item = CartItem.objects.get(user=request.user, product_id=target)
    except CartItem.DoesNotExist:
        busqueda_item = None
    busqueda_item.delete()
    
    return HttpResponseRedirect(reverse('cart'))

def limpiar_carrito(request):
    try:
        busqueda_item = CartItem.objects.filter(user=request.user)
    except CartItem.DoesNotExist:
        busqueda_item = None
    busqueda_item.delete()

    return HttpResponseRedirect(reverse('cart'))

def confirmar_carrito(request):
    try:
        busqueda_item = CartItem.objects.filter(user=request.user, confirmado=False)
    except CartItem.DoesNotExist:
        busqueda_item = None
    if busqueda_item:
        busqueda_item.update(confirmado=True)
    
    return HttpResponseRedirect(reverse('cart'))