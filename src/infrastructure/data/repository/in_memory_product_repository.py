from typing import List

from src.core.entities.product import Product
from src.core.interfaces.product_repository import IProductRepository


class InMemoryProductRepository(IProductRepository):

    def __init__(self, products: List[Product] = None):
        self._products = {p.id: p for p in products}

    def get_all(self) -> List[Product]:
        return list(self._products.values())

    def get_product(self, product_id: int) -> Product:
        product = self._products[product_id]
        return product

    def create_product(self, product: Product) -> None:
        if product.id in self._products:
            raise ValueError(f"Cannot create new product - a product already exists for id '{product.id}'!")

        self._products[product.id] = product

    def update_product(self, product: Product) -> None:
        if product.id not in self._products:
            raise ValueError(f"Cannot update product - no product exists for id '{product.id}'!")

        self._products[product.id] = product

    def delete_product(self, product_id: int) -> None:
        if product_id not in self._products:
            raise ValueError(f"Cannot delete product - no product exists for id '{product_id}'!")

        del self._products[product_id]
