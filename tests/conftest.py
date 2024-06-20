import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from taskmaster.core.config import Settings
from taskmaster.core.database import get_session
from taskmaster.main import app
from taskmaster.models import Base


@pytest.fixture(scope='session')
def engine():
    _engine = create_engine(Settings().DATABASE_URL.unicode_string())

    with _engine.begin():
        yield _engine


@pytest.fixture()
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture()
def session(engine):
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session
        session.rollback()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
