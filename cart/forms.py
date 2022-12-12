from django import forms
from cart.models import CartItem

class CartForm(forms.ModelForm):
    # cantidad = forms.IntegerField(
    #     widget=forms.NumberInput(
    #         attrs= {
    #             'class': 'form-control',
    #             'placeholder': 'ej: 10'
    #         }
    #     )
    # )

    class Meta:
        model = CartItem
        fields = ('cantidad',)
        
       