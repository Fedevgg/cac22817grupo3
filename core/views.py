from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def index(request):
    return render(request, "core/index.html")

def contact(request):
    data = {
        'form': ContactForm()
    }
    return render(request, 'core/contact.html', data)