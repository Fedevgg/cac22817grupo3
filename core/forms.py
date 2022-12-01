from django import forms
from .models import Contact
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'


class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
