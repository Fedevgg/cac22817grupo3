from django.shortcuts import render
#from cac22817grupo3 import products

# Create your views here.

def index(request):
    return render(request, "core/index.html")

def page2(request):
    return render(request, 'core/page2.html')