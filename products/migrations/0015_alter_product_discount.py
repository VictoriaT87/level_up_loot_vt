# Generated by Django 3.2.18 on 2023-05-29 15:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0014_alter_product_discount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="discount",
            field=models.IntegerField(default=10, help_text="Discount in Percentage"),
        ),
    ]
