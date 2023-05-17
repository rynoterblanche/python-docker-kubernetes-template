from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory, Singleton, Configuration

from src.infrastructure.data.orm.database import Database
from src.infrastructure.data.repository.sql_alchemy_product_repository import SqlAlchemyProductRepository


class AppContainer(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        packages=[
            ".controllers",
        ],
    )

    config = Configuration(yaml_files=["/config/config.yml"])

    db = Singleton(Database, db_url=config.db.url)

    product_repository = Factory(SqlAlchemyProductRepository,
                                 session_factory=db.provided.session)
