from django.test import TestCase
from .modeels import Product

class ProductModelTest(TesCase):
    def test_create_product(self):
        product = Product.objects.create(
            name = "Arroz",
            price = 5.50,
            weight = 1.0,
            experation_date = "2024-12-31",
            category = "Alimentos"
        )
        self.assertEqual(product.name, "Arroz")
        self.assertEqual(product.price, 5.50)
        self.assertEqual(product.weight, 1.0)
        self.assertEqual(product.category, "Alimentos")

    def test_create_product_without_name(self):
        with self.assertRaises(ValueError)
            Product.objects.create(
                name = "",
                price = 5.50,
                weight = 1.0,
                experation_date = "2024-12-31",
                category = "Alimentos"
            )
