from flask import Flask

from src.product_service.containers import AppContainer
from src.product_service.extensions.register_routes import register_routes

if __name__ == "__main__":
    container = AppContainer()
    container.init_resources()

    db = container.db()
    db.create_database()

    app = Flask(__name__)
    app.container = container

    register_routes(app)

    app.run(debug=True, host="0.0.0.0")
