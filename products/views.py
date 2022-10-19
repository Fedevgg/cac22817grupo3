from django.shortcuts import render

# Create your views here.

def page1(request):
    #productForSlide = products.objects.all()
    return render(request, 'products/page1.html')