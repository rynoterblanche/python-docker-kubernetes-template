class Product:

    def __init__(self, product_id: int, name: str):
        self._id = product_id
        self._name = name

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    def __repr__(self):
        return f"Product: [id='{self.id}'; name='{self.name}']"
