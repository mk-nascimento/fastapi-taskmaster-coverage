from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from taskmaster.enums.todo_enums import TodoStatus


class ID(BaseModel):
    id: int


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TodoStatus


class TodoCreate(TodoBase): ...


class Todo(ID, TodoBase):
    model_config = ConfigDict(from_attributes=True)

    created_at: datetime
