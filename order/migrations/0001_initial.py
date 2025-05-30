# Generated by Django 5.1.4 on 2025-01-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('customer_name', models.CharField(max_length=255)),
                ('shipping_address', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('whatsapp', models.CharField(max_length=15)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
