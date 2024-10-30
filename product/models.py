from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))  # Preço de custo
    stock_quantity = models.PositiveIntegerField()
    sku = models.CharField(max_length=50, unique=True)
    batch_number = models.CharField(max_length=50, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    supplier = models.CharField(max_length=100)
    supplier_email = models.EmailField(blank=True, null=True)
    supplier_phone = models.CharField(max_length=20, blank=True, null=True)
    barcode = models.CharField(max_length=13, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

class Meta:
    ordering = ['name']
    indexes = [
        models.Index(fields= ['sku']),
        models.Index(fields=['name']),
    ]

def __str__(self):
    return f"{self.name ({self.sku})}"

def clean(self):
    # Validação para garantir que a data de validade não esteja no passado
    if self.expiration_date and self.expiration_date < timezone.now().date():
        raise ValidationError("A data de validade não pode ser no passado.")

def get_margin(self):
    # Calcula a margem de lucro com base no preço de custo e preço de venda
    if self.cost_price and self.price:
        return self.price - self.cost_price
    return Decimal("0.00")

def decrease_stock(self):
    # Deminui o estoque, evitando valores negativos
    if quantity > self.stock_quantity:
        raise ValidationError("Estoque insuficiente para a quantidade solicitada.")
    self.stock_quantity -= quantity
    self.save()

def increase_stock(self):
    # Aumenta o estoque do produto
    self.stock_quantity += qunaity
    self.save()
    
def save(self, *args, **kwargs):
    # Garante que o SKU seja imutável após a criação
    if self.pk:
        original = Product.objects.get(pk=self.pk)
        if original.sku != self.sku:
            raise ValidationError("O SKU não pode ser alterado após a criaçõa.")
        
    super().save(*args, **kwargs)