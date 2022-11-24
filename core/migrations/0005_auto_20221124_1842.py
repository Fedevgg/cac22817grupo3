# Generated by Django 3.2 on 2022-11-24 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='consulta',
        ),
        migrations.AddField(
            model_name='contact',
            name='apellido',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='edad',
            field=models.SmallIntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='solicitud',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
