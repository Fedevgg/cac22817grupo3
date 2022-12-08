from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from products.models import Product
from django.http import HttpResponse
from .cart import Cart

def cart_page(request):
     return render(request, "cart\templates\cart.html")

def add_product(request, producto_id):
    cart = Cart(request)
    producto = Product.objects.get(id=producto_id)
    cart.add(producto)
    return redirect("catalog")

def delete_product(request, producto_id):
    cart = Cart(request)
    producto = Product.objects.get(id=producto_id)
    cart.delete(producto)
    return redirect("catalog")

def decrement_product(request, producto_id):
    cart = Cart(request)
    producto = Product.objects.get(id=producto_id)
    cart.decrement(producto)
    return redirect("catalog")

def clean_cart(request):
    cart = Cart(request)
    cart.clean_cart()
    return redirect("catalog")