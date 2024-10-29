from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    sku = models.CharField(max_length=50, unique=True)  # Código de produto exclusivo
    batch_number = models.CharField(max_length=50, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.sku})"
