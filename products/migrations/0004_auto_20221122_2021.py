# Generated by Django 3.2 on 2022-11-22 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_client_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='productsImages'),
        ),
    ]