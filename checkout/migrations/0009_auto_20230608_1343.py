# Generated by Django 3.2.18 on 2023-06-08 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_auto_20230607_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='max_value',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='used',
        ),
    ]
