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

    def test_sku_field_immutable(self):
        # Teste para garantir que o campo 'sku' não seja alterável após a criação
        # product = Product.objects.get(sku="TEST123")
        original_sku = self.product.sku
        self.product.sku = "NOVOSKU"
        self.product.save()
        # Recarrega o produto do banco de para ver se o sku foi alterado
        self.product.refresh_from_db()
        self.assertEqual(self.product.sku, oiginal_sku) # O sku deve permanecer com "TEST123"

    # Atualizaçõa de Estoque
    def test_stock_quantity_increase(self):
        # Teste para aumentar a quantidade de estoque
        # product = Product.objects.get(sku="TEST123")
        original_stock = self.product.stock_quantity
        self.additional_stock = 10
        self.product.stock_quantity += addtional_stock
        self.product.save()
        self.product.refresh_from_db()
        self.assertEqual(product.stock_quantity, original_stock + additional_stock)

    def test_stock_quantity_decrease(self):
        # Teste para diminiur a quantidade de produtos no estoque
        # product = Product.objects.get(sku="TEST123")
        self.original_stock = product.stock_quantity
        self.removed_stock = 5
        self.product.stock_quantity -= removed_stock
        self.product.save()
        self.product.refresh_from_db()
        self.assertEqual(product.stock_quantity, original_stock - removed_sock)

    def test_stock_quantity_negative(Self):
        # Teste para garantir que o estoque não fique negativo
        with self.assertRaises(ValidationError):
            self.product.stock_quantity = -5
            self.prodcut.full_clean()

    
    
class ProductModelTest(TestCase):

    # Outros testes já existentes aqui...

    def test_sku_field_immutable(self):
        """Teste para garantir que o campo 'sku' não seja alterável após criação."""
        product = Product.objects.get(sku="TEST123")
        original_sku = product.sku
        product.sku = "NOVOSKU456"
        product.save()
        product.refresh_from_db()
        self.assertEqual(product.sku, original_sku)

    def test_stock_quantity_increase(self):
        """Teste para aumentar a quantidade de estoque."""
        product = Product.objects.get(sku="TEST123")
        original_stock = product.stock_quantity
        additional_stock = 10
        product.stock_quantity += additional_stock
        product.save()
        product.refresh_from_db()
        self.assertEqual(product.stock_quantity, original_stock + additional_stock)

    def test_stock_quantity_decrease(self):
        """Teste para diminuir a quantidade de estoque."""
        product = Product.objects.get(sku="TEST123")
        original_stock = product.stock_quantity
        removed_stock = 5
        product.stock_quantity -= removed_stock
        product.save()
        product.refresh_from_db()
        self.assertEqual(product.stock_quantity, original_stock - removed_stock)

    def test_stock_quantity_negative(self):
        """Teste para garantir que o estoque não fique negativo."""
        product = Product.objects.get(sku="TEST123")
        product.stock_quantity = -1
        with self.assertRaises(ValidationError):
            product.full_clean()


