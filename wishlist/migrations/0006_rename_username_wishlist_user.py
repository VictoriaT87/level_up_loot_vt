# Generated by Django 3.2.18 on 2023-05-21 14:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("wishlist", "0005_auto_20230521_1412"),
    ]

    operations = [
        migrations.RenameField(
            model_name="wishlist",
            old_name="username",
            new_name="user",
        ),
    ]
