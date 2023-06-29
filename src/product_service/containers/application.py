from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory, Singleton, Configuration, Resource, Callable, Container

import logging.config

from src.product_service.containers.gateways import GatewaysContainer
from src.product_service.containers.services import ServicesContainer


class AppContainer(DeclarativeContainer):
    config = Configuration()

    wiring_config = WiringConfiguration(
        packages=[
            "src.product_service.controllers",
        ],
    )

    logging = Resource(
        logging.config.dictConfig,
        config=config.logging,
    )

    gateways = Container(
        GatewaysContainer,
        config=config,
    )

    services = Container(
        ServicesContainer,
        gateways=gateways,
    )
