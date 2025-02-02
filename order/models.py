from django.db import models

class Order(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    customer_name = models.CharField(max_length=255, default="Unknown")  # Add a default value if needed
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

