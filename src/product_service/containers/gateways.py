from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Callable, Singleton

from src.infrastructure.data.orm.database import Database
from src.shared.environment import Env


def get_database_url(config: Configuration):
    db_config = config["db"]
    db_url = db_config["url"]

    if "{db_user}" in db_url:
        db_user = Env.get("PRODUCTS_DB_USER")
        db_url = db_url.replace("{db_user}", db_user)

    if "{db_password}" in db_url:
        db_password = Env.get("PRODUCTS_DB_PASSWORD")
        db_url = db_url.replace("{db_password}", db_password)

    return db_url


class GatewaysContainer(DeclarativeContainer):
    config = Configuration()

    db_url = Callable(get_database_url, config=config)
    db = Singleton(Database, db_url=db_url)
