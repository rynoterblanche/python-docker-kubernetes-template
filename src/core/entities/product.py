class Product:
    id: int
    name: str

    def __init__(self, product_id: int, name: str):
        self.id = product_id
        self.name = name

    def __repr__(self):
        return f"Product: [id='{self.id}'; name='{self.name}']"
