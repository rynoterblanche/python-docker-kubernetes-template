import logging
from contextlib import contextmanager, AbstractContextManager
from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session, Session

logger = logging.getLogger(__name__)

Base = declarative_base()


class Database:

    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(
            db_url
        )
        self._session_factory = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()
