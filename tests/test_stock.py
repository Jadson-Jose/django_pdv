from django.test import TestCase
from .models import Product

class StockUpdateTest(TestCase):
    def setUp(self):
        # Setup inicial de um produto inicial para ser usado nos testes
        self.product = Product.objects.create(
            name = "Arroz",
            price = 5.50,
            weight = 1.0,
            experation_date = "2024-12-31",
            category = "Alimentos",
            stock_quantity = 100
        )
    
    def test_stock_decreases_after_sale(self):
        # Simula uma venda de 10 unidades
        self.product.sell(quantity= 10)
        self.assertEqual(self.product.stock_quantity, 90)

    def test_error_on_insufficient_stock(self):
        # Tenta vender mais do que o disponível no estoque
        with self.assertRaises(ValueError):
            self.product.sell(quantity = 200)
