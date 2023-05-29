from src.product_service.controllers.product import ProductListController, ProductController


def register_routes(app):
    app.add_url_rule("/products", view_func=ProductListController.as_view("product-list"))
    app.add_url_rule("/products/<int:product_id>", view_func=ProductController.as_view("product"))
