from src.core.entities.product import Product
from src.infrastructure.data.orm.models.product_model import ProductModel


class ProductOrmEntityMapper(object):
    """A very rudimentary mapper between ORM and domain objects

    A better mapping solution should be considered at some point.
    """

    @staticmethod
    def map_to_entity(model: ProductModel) -> Product:
        return Product(product_id=model.id,
                       name=model.name)

    @staticmethod
    def map_to_model(product: Product) -> ProductModel:
        return ProductModel(id=product.id,
                            name=product.name)
