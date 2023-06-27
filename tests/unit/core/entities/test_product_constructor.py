from unittest import TestCase

from src.core.entities.product import Product


class TestProductConstructor(TestCase):

    def setUp(self) -> None:
        self.product = Product(123, "ABC")

    def test_constructor_initialises_id(self):
        self.assertEqual(123, self.product.id)

    def test_constructor_initialises_name(self):
        self.assertEqual("ABC", self.product.name)

    def test_product_repr(self):
        self.assertEqual("Product: [id='123'; name='ABC']", str(self.product))
