from typing import Optional

from flask import Flask

from src.product_service.containers import AppContainer
from src.product_service.extensions.register_routes import register_routes


def create_app(config: Optional[dict] = None):
    container = AppContainer()
    if config:
        container.config.from_dict(config)

    container.init_resources()

    db = container.db()
    db.create_database()

    app = Flask(__name__)
    app.container = container

    register_routes(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0")
