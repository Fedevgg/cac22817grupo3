from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmado = models.BooleanField(default=False)
    
    # Quiero que devuelva la cantidad y el nombre
    def __str__(self):
        return f'{self.cantidad} unidades de {self.product_id.name}'

    class Meta:
        db_table = 'cart_item'
        verbose_name = 'cart item'
        verbose_name_plural = 'cart items'
        ordering = ['id']

class PedidoConfirmado(models.Model):
    estado = models.BooleanField()
    cart = models.OneToOneField(CartItem, on_delete=models.CASCADE)

    class Meta:
            db_table = 'pedidos'
            verbose_name = 'pedido'
            verbose_name_plural = 'pedidos'
            ordering = ['id']