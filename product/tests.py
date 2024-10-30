from django.test import TestCase
from django.core.exceptions import ValidationError
from decimal import Decimal
from .models import Product, Category

class ProductModelCreationTest(TestCase):
    
    def setUp(self):
        # Criando uma categoria para associar ao produto
        self.category = Category.objects.create(name="Categoria Teste")
    
    def test_product_creation_with_all_fields(self):
        """Verifica a criação de um produto com todos os campos preenchidos, incluindo os opcionais."""
        product = Product.objects.create(
            name="Produto Completo",
            description="Descrição do produto completo",
            price=Decimal("19.99"),
            cost_price=Decimal("10.00"),
            stock_quantity=100,
            sku="COMPLETE123",
            batch_number="BATCH100",
            expiration_date="2025-12-31",
            supplier="Fornecedor Completo",
            category=self.category
        )
        
        # Verificações
        self.assertEqual(Product.objects.count(), 1)  # Verifica se o produto foi criado
        self.assertEqual(product.name, "Produto Completo")
        self.assertEqual(product.description, "Descrição do produto completo")
        self.assertEqual(product.stock_quantity, 100)
        self.assertEqual(product.sku, "COMPLETE123")

    def test_product_creation_missing_required_fields(self):
        """Verifica que a criação de um produto sem os campos obrigatórios gera um ValidationError."""
        product = Product(
            description="Descrição sem nome e preço",
            stock_quantity=10,
            sku="INCOMPLETE123",
            supplier="Fornecedor Incompleto",
            category=self.category
        )
        
        # O método full_clean() deve levantar um ValidationError ao faltar campos obrigatórios
        with self.assertRaises(ValidationError):
            product.full_clean()
