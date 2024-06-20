from enum import Enum


class TodoStatus(str, Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'in progress'
    COMPLETED = 'completed'
