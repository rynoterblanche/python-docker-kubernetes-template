import logging
from contextlib import AbstractContextManager
from typing import List, Callable

from dependency_injector.wiring import inject
from sqlalchemy.orm import Session

from src.core.entities.product import Product
from src.core.interfaces.product_repository import IProductRepository
from src.infrastructure.data.errors.not_found_error import NotFoundError
from src.infrastructure.data.orm.mappers.product_orm_entity_mapper import ProductOrmEntityMapper
from src.infrastructure.data.orm.models.product_model import ProductModel


class SqlAlchemyProductRepository(IProductRepository):

    @inject
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self._session_factory = session_factory
        self._logger = logging.getLogger(__name__)

    def get_all(self) -> List[Product]:
        self._logger.debug("Query all products")
        with self._session_factory() as session:
            rows = session.query(ProductModel).all()
            products = [ProductOrmEntityMapper.map_to_entity(row) for row in rows]
            return products

    def get_product(self, product_id: int) -> Product:
        self._logger.debug(f"Find product by id '{product_id}'")
        with self._session_factory() as session:
            instance = session.get(ProductModel, product_id)
            if not instance:
                raise ProductNotFoundError(product_id)
            product = ProductOrmEntityMapper.map_to_entity(instance)
            return product

    def create_product(self, product: Product) -> None:
        self._logger.debug(f"Create product : '{product}'")
        with self._session_factory() as session:
            model = ProductOrmEntityMapper.map_to_model(product)
            session.add(model)
            session.commit()
            session.refresh(model)

    def update_product(self, product: Product) -> None:
        self._logger.debug(f"Update product by id  : '{product}'")
        with self._session_factory() as session:
            instance = session.query(ProductModel).get(product.id)
            if not instance:
                raise ProductNotFoundError(product.id)
            instance.name = product.name
            session.commit()

    def delete_product(self, product_id: int) -> None:
        self._logger.debug(f"Delete product by id '{product_id}'")
        with self._session_factory() as session:
            instance = session.query(ProductModel).get(product_id)
            if not instance:
                raise ProductNotFoundError(product_id)
            session.delete(instance)
            session.commit()


class ProductNotFoundError(NotFoundError):
    entity_name: str = "Product"
