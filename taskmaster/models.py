from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Enum, Integer, String
from sqlalchemy.orm import DeclarativeBase

from taskmaster.enums.todo_enums import TodoStatus

UTC = timezone.utc


class Base(DeclarativeBase): ...


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String(48), nullable=False, unique=True)
    description = Column(String(128), nullable=True)
    status = Column(Enum(TodoStatus), default=TodoStatus.PENDING, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC), nullable=False)
