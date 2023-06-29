import pytest

from src.product_service.app import create_app
from tests.functional.product_service.app_container import TestAppContainer
from tests.functional.product_service.app_seed_data import SeedData


@pytest.fixture(scope="package")
def app():
    container = TestAppContainer()
    container.init_resources()

    db = container.gateways.db()
    db.create_database()

    SeedData.populate_test_data(db)

    app = create_app()
    app.container = container

    yield app

    app.container.unwire()


@pytest.fixture(scope="package")
def client(app):
    return app.test_client()
