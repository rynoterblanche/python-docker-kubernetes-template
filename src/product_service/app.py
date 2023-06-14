from argparse import ArgumentParser

from flask import Flask

from src.product_service.containers import AppContainer
from src.product_service.extensions.register_routes import register_routes


def create_app(config) -> Flask:
    container = AppContainer()
    container.config.from_yaml(config)

    container.init_resources()

    db = container.db()
    db.create_database()

    app = Flask(__name__)
    app.container = container

    register_routes(app)

    return app


if __name__ == "__main__":
    default_config_path = "/config/config.yml"

    parser = ArgumentParser(
        prog="ProductService",
        description="RESTful API to Products.")
    parser.add_argument(
        "--config",
        required=False,
        default=default_config_path,
        help=f"Defaults to `{default_config_path}` if not provided.")

    args = parser.parse_args()

    config_source = args.config

    app = create_app(config_source)
    app.run(debug=True, host="0.0.0.0")
