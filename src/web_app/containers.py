from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory

from src.core.entities.product import Product
from src.infrastructure.data.repository.in_memory_product_repository import InMemoryProductRepository


class AppContainer(DeclarativeContainer):
    products = [
        Product(1, "PS4"),
        Product(2, "PS5"),
    ]

    wiring_config = WiringConfiguration(
        packages=[
            ".controllers",
        ],
    )

    product_repository = Factory(InMemoryProductRepository,
                                 products=products)
