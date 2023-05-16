from sqlalchemy import Column, Integer, String

from src.infrastructure.data.orm.database import Base


class ProductModel(Base):
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), index=True)
