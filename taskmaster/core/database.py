from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session as SaSession

from taskmaster.core.config import Settings

env = Settings()

engine = create_engine(env.DATABASE_URL.unicode_string())


def get_session():
    with SaSession(engine) as session:
        yield session


Session = Annotated[SaSession, Depends(get_session)]
