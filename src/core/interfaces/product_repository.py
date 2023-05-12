from abc import ABC, abstractmethod
from typing import List

from src.core.entities.product import Product


class IProductRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Product]:
        raise NotImplementedError

    @abstractmethod
    def get_product(self, product_id: int) -> Product:
        raise NotImplementedError

    @abstractmethod
    def create_product(self, product: Product) -> None:
        raise NotImplementedError

    @abstractmethod
    def update_product(self, product: Product) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete_product(self, product_id: int) -> None:
        raise NotImplementedError
