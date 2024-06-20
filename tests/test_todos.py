from fastapi import status

from taskmaster.enums.todo_enums import TodoStatus
from taskmaster.schemas import Todo, TodoCreate
from tests.factories import TodoFactory

_PATH = '/api/v0/todos'


def test_create_todo(client):
    _todo = TodoCreate(title='Todo Test', status=TodoStatus.PENDING)

    res = client.post(_PATH, json=_todo.model_dump())

    assert res.status_code == status.HTTP_201_CREATED
    assert Todo.model_validate_json(res.text)


def test_read_todos(session, client):
    EXPECTED = 5
    session.bulk_save_objects(TodoFactory.build_batch(EXPECTED))
    session.commit()

    res = client.get(_PATH)
    todos = res.json()

    assert res.status_code == status.HTTP_200_OK
    assert len(todos) == EXPECTED
    for todo in todos:
        assert Todo.model_validate(todo)


def test_read_paginated_todos(session, client):
    EXPECTED = 2
    session.bulk_save_objects(TodoFactory.build_batch(EXPECTED))
    session.commit()

    res = client.get(f'{_PATH}?limit={EXPECTED}')
    todos = res.json()

    assert res.status_code == status.HTTP_200_OK
    assert len(todos) == EXPECTED
    for todo in todos:
        assert Todo.model_validate(todo)


def test_read_todo_by_id(session, client):
    session.bulk_save_objects(TodoFactory.build_batch(3))
    session.commit()

    res = client.get(f'{_PATH}/2')

    assert res.status_code == status.HTTP_200_OK
    assert Todo.model_validate_json(res.text)


def test_read_non_existent_todo(client):
    res = client.get(f'{_PATH}/999')

    assert res.status_code == status.HTTP_404_NOT_FOUND
    assert 'Todo #999 not found' in res.text


def test_update_non_existent_todo(client):
    res = client.put(f'{_PATH}/999', json={'title': '', 'status': 'completed'})

    assert res.status_code == status.HTTP_404_NOT_FOUND
    assert 'Todo #999 not found' in res.text


def test_update_todo(session, client):
    session.bulk_save_objects(TodoFactory.build_batch(3))
    session.commit()

    res = client.put(f'{_PATH}/2', json={'title': 'Doing', 'status': 'in progress'})

    assert res.status_code == status.HTTP_200_OK
    assert Todo.model_validate_json(res.text)
    assert res.json()['title'] == 'Doing'
    assert res.json()['status'] == 'in progress'


def test_delete_non_existent_todo(client):
    res = client.delete(f'{_PATH}/999')

    assert res.status_code == status.HTTP_404_NOT_FOUND
    assert 'Todo #999 not found' in res.text


def test_delete_todo(session, client):
    session.bulk_save_objects(TodoFactory.build_batch(3))
    session.commit()

    res = client.delete(f'{_PATH}/2')

    assert res.status_code == status.HTTP_204_NO_CONTENT
    assert not res.text
