# Generated by Django 3.2 on 2022-12-12 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_pedidoconfirmado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidoconfirmado',
            old_name='cart_id',
            new_name='cart',
        ),
    ]
