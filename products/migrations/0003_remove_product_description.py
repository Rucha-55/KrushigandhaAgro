# Generated by Django 5.1.4 on 2025-01-16 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
