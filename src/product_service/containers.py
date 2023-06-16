from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory, Singleton, Configuration, Resource, Callable

import logging.config

from src.infrastructure.data.orm.database import Database
from src.infrastructure.data.repository.sql_alchemy_product_repository import SqlAlchemyProductRepository
from src.shared.environment import Env


def get_database_url(config: Configuration):
    db_config = config["db"]
    db_url = db_config["url"]

    if "{db_user}" in db_url:
        db_user = Env.get("PRODUCTS_DB_USER")
        db_url = db_url.replace("{db_user}", db_user)

    if "{db_password}" in db_url:
        db_password = Env.get("PRODUCTS_DB_PASSWORD")
        db_url = db_url.replace("{db_password}", db_password)

    return db_url


class AppContainer(DeclarativeContainer):
    config = Configuration(yaml_files=["/config/config.yml"])

    wiring_config = WiringConfiguration(
        packages=[
            ".controllers",
        ],
    )

    logging = Resource(
        logging.config.dictConfig,
        config=config.logging,
    )

    db_url = Callable(get_database_url, config=config)
    db = Singleton(Database, db_url=db_url)

    product_repository = Factory(SqlAlchemyProductRepository,
                                 session_factory=db.provided.session)
