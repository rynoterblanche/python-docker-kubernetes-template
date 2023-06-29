from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Container

from src.product_service.containers.gateways import GatewaysContainer
from src.product_service.containers.services import ServicesContainer


class TestAppContainer(DeclarativeContainer):
    test_config = {
        "db": {
            "url": "sqlite:///:memory:"
        }
    }

    wiring_config = WiringConfiguration(
        packages=[
            "src.product_service.controllers"
        ],
    )

    gateways = Container(
        GatewaysContainer,
        config=test_config,
    )

    services = Container(
        ServicesContainer,
        gateways=gateways,
    )
