from django.shortcuts import render
from .models import Product
# Create your views here.

def page1(request):
    products = Product.objects.all()
    return render(request, 'products/page1.html',{'products': products})