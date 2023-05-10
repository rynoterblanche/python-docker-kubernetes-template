from flask import Flask, jsonify, request

from src.core.entities.product import Product

products = [
    Product(1, "PS4"),
    Product(2, "PS5"),
]

app = Flask(__name__)


@app.route("/products")
def get_products():
    product_list_response = [{"id": p.id, "name": p.name} for p in products]

    return jsonify(product_list_response)


@app.route("/product/<int:id>")
def get_product(id):
    product = next(filter(lambda p: p.id == id, products), None)
    if product is None:
        return f"Product with id '{id}' not found!", 404

    product_response = {"id": product.id, "name": product.name}
    return jsonify(product_response)


@app.route("/product", methods=["POST"])
def create_product():
    create_request = request.json

    new_id = max(product.id for product in products) + 1
    new_product = Product(new_id, create_request["name"])
    products.append(new_product)

    return jsonify(new_product), 201


@app.route("/product/<int:id>", methods=["PUT"])
def update_product():
    update_request = request.json

    product = next(filter(lambda p: p.id == id, products), None)
    if product is None:
        return f"Product with id '{id}' not found!", 404

    product.name = update_request["name"]
    return jsonify(product), 200


@app.route("/product/<int:id>", methods=["DELETE"])
def delete_product():
    product = next(filter(lambda p: p.id == id, products), None)
    if product is None:
        return f"Product with id '{id}' not found!", 404

    products.remove(product)
    return f"Product with id '{id}' deleted!", 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
