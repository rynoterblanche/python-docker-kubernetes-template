from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory, Singleton, Configuration, Resource, Callable

import logging.config

from src.infrastructure.data.orm.database import Database
from src.infrastructure.data.repository.sql_alchemy_product_repository import SqlAlchemyProductRepository
from src.web_app.environment import Env


def get_database_url(db_config: Configuration):
    product_service = db_config["product_service"]
    username = product_service["username"]
    host = product_service["host"]
    database = product_service["database"]
    password = Env.get("MYSQL_USER_PASSWORD")
    db_url = f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"
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

    db_url = Callable(get_database_url, db_config=config.db)
    db = Singleton(Database, db_url=db_url)

    product_repository = Factory(SqlAlchemyProductRepository,
                                 session_factory=db.provided.session)
