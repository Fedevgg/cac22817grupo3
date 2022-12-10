from django.shortcuts import render, redirect

# Create your views here.
from products.models import Product
from .cart import Cart

def cart_page(request):
    products = Product.objects.all()
    return render(request, 'cart/cart.html', {'products':products})

def add_product(request, product_id):
    cart = Cart(request)
    producto = Product.objects.get(id=product_id)
    cart.add(producto)
    return redirect("catalog")

def delete_product(request, product_id):
    cart = Cart(request)
    producto = Product.objects.get(id=product_id)
    cart.delete(producto)
    return redirect("catalog")

def decrement_product(request, product_id):
    cart = Cart(request)
    producto = Product.objects.get(id=product_id)
    cart.decrement(producto)
    return redirect("catalog")

def clean_cart(request):
    cart = Cart(request)
    cart.clean_cart()
    return redirect("catalog")


