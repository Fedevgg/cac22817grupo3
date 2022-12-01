from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from core.forms import RegistrarUsuarioForm


# Create your views here.

def index(request):
    return render(request, "core/index.html")

def contact(request):
    data = {
        'form': ContactForm()
    }
    return render(request, 'core/contact.html', data)

def core_registrarse(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'core/registrarse.html', {'form': form, 'title': 'registrese aquí'})


def core_login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Bienvenido/a {username} !!')
            return redirect('home')
        else:
            messages.error(request, f'Cuenta o password incorrecto, realice el login correctamente')
    
    form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form, 'title': 'Log in'})


def compras(request):
    return render(request, "core/compras.html")