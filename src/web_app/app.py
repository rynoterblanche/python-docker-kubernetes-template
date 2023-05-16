from flask import Flask

from src.web_app.containers import AppContainer
from src.web_app.extensions.register_routes import register_routes

if __name__ == "__main__":
    container = AppContainer()

    db = container.db()
    db.create_database()

    app = Flask(__name__)
    app.container = container

    register_routes(app)

    app.run(debug=True, host="0.0.0.0")
