from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import DependenciesContainer, Factory

from src.infrastructure.data.repository.sql_alchemy_product_repository import SqlAlchemyProductRepository


class ServicesContainer(DeclarativeContainer):
    gateways = DependenciesContainer()

    product_repository = Factory(SqlAlchemyProductRepository,
                                 session_factory=gateways.db.provided.session)
