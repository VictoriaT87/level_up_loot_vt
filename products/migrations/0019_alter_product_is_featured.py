# Generated by Django 3.2.18 on 2023-06-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='Is Featured on Index Page?'),
        ),
    ]
