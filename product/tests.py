from django.test import TestCase
from django.core.exceptions import ValidationError
from decimal import Decimal
from .models import Product

class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Produto Teste",
            description="Descrição do produto teste",
            price=Decimal("19.99"),
            stock_quantity=50,
            sku="TEST123",
            batch_number="BATCH001",
            expiration_date="2025-12-31",
            supplier="Fornecedor Teste"
        )

    def test_product_creation_without_required_fields(self):
        product = Product(price=Decimal("9.99"), stock_quantity=10)  # Criar instância sem 'name', 'sku' e 'supplier'
        with self.assertRaises(ValidationError):  # Esperar um ValidationError
            product.full_clean()  # O método full_clean() deve levantar uma ValidationError
            product.save()  # O save() não deve ser alcançado se a validação falhar

    def test_product_creation(self):
        product = Product.objects.get(sku="TEST123")
        self.assertEqual(product.name, "Produto Teste")
        self.assertEqual(product.price, Decimal("19.99"))
        self.assertEqual(product.stock_quantity, 50)
        self.assertEqual(product.supplier, "Fornecedor Teste")

    def test_product_update(self):
        product = Product.objects.get(sku="TEST123")
        product.name = "Produto Atualizado"
        product.save()
        self.assertEqual(Product.objects.get(sku="TEST123").name, "Produto Atualizado")

    def test_product_deletion(self):
        product = Product.objects.get(sku="TEST123")
        product.delete()
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(sku="TEST123")

    def test_product_string_representation(self):
        product = Product.objects.get(sku="TEST123")
        self.assertEqual(str(product), "Produto Teste (TEST123)")
