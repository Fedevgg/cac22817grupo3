from django.shortcuts import render
#from cac22817grupo3 import products

# Create your views here.

def index(request):
    return render(request, "core/index.html")
'''
def home(request):
    art=Arte.objects.all()
    try:
        objeto_especifico = Arte.objects.get(pk=1) # Cambiar por el parametro deseado, pk, codename unico, etc
    except Arte.DoesNotExist:
        objeto_especifico = None
    return render(request, "AppGaleria/home.html", {"arte": art, 'objeto_especifico': objeto_especifico})
'''

def page1(request):
    #productForSlide = products.objects.all()
    return render(request, 'core/page1.html')

def page2(request):
    return render(request, 'core/page2.html')