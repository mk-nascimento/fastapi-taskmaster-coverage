from factory import Factory, Faker
from factory.fuzzy import FuzzyChoice

from taskmaster.enums.todo_enums import TodoStatus
from taskmaster.models import Todo


class TodoFactory(Factory):
    class Meta:
        model = Todo

    title = Faker('text', max_nb_chars=48)
    description = Faker('text', max_nb_chars=128)
    status = FuzzyChoice(TodoStatus)
