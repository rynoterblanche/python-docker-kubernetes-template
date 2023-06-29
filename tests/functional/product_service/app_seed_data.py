from src.infrastructure.data.orm.database import Database
from src.infrastructure.data.orm.models.product_model import ProductModel


class SeedData:
    product_test_data = [
        ProductModel(id=1, name="Product A"),
        ProductModel(id=2, name="Product B"),
        ProductModel(id=3, name="Product C")
    ]

    @staticmethod
    def populate_test_data(db: Database):
        with db.session() as session:
            for product in SeedData.product_test_data:
                session.add(product)
            session.commit()
