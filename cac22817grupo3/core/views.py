from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def page1(request):
    return render(request, 'core/page1.html')

def page2(request):
    return render(request, 'core/page2.html')