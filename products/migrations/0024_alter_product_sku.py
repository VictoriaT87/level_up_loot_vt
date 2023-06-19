# Generated by Django 3.2.18 on 2023-06-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, help_text='SKU must be 6 digits', max_length=6, null=True, unique=True, verbose_name='Sku must be a 6 digit unique code'),
        ),
    ]
