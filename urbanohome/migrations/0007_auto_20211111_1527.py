# Generated by Django 3.2.9 on 2021-11-11 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urbanohome', '0006_auto_20211111_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='venta',
        ),
        migrations.AddField(
            model_name='venta',
            name='productoId',
            field=models.ManyToManyField(blank=True, to='urbanohome.Producto'),
        ),
    ]