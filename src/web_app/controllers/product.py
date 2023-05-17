import logging

from dependency_injector.wiring import inject, Provide
from flask import jsonify, request
from flask.views import MethodView

from src.core.entities.product import Product
from src.core.interfaces.product_repository import IProductRepository
from src.infrastructure.data.repository.sql_alchemy_product_repository import ProductNotFoundError
from src.web_app.containers import AppContainer

log = logging.getLogger(__name__)


class ProductListController(MethodView):

    @inject
    def __init__(self, product_repository: IProductRepository = Provide[AppContainer.product_repository]):
        self._product_repository = product_repository

    def get(self):
        log.debug("GET /products")
        product_list_response = [{"id": p.id, "name": p.name} for p in self._product_repository.get_all()]
        return jsonify(product_list_response)

    def post(self):
        create_request = request.json

        log.debug(f"POST /products : {create_request}")

        new_id = max([product.id for product in self._product_repository.get_all()], default=0) + 1
        new_product = Product(new_id, create_request["name"])
        self._product_repository.create_product(new_product)

        new_product_response = {
            "id": new_product.id,
            "name": new_product.name
        }
        return jsonify(new_product_response), 201


class ProductController(MethodView):

    @inject
    def __init__(self, product_repository: IProductRepository = Provide[AppContainer.product_repository]):
        self._product_repository = product_repository

    def get(self, product_id):
        log.debug(f"GET /products/{product_id}")

        try:
            product = self._product_repository.get_product(product_id)
        except ProductNotFoundError:
            return f"Product with id '{product_id}' not found!", 404

        product_response = {"id": product.id, "name": product.name}
        return jsonify(product_response)

    def patch(self, product_id):
        update_request = request.json

        log.debug(f"PATCH /products/{product_id} : {update_request}")

        try:
            product = self._product_repository.get_product(product_id)
        except ProductNotFoundError:
            return f"Product with id '{product_id}' not found!", 404

        product.name = update_request["name"]
        self._product_repository.update_product(product)

        patched_product_response = {"id": product.id, "name": product.name}
        return jsonify(patched_product_response), 200

    def delete(self, product_id):
        log.debug(f"DELETE /products/{product_id}")

        try:
            self._product_repository.delete_product(product_id)
            return f"Product with id '{product_id}' deleted!", 200
        except ProductNotFoundError:
            return f"Product with id '{product_id}' not found!", 404
