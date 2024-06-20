from fastapi import APIRouter, Query, status
from sqlalchemy import select

from taskmaster import models
from taskmaster.core.database import Session
from taskmaster.core.exceptions import NotFoundException
from taskmaster.schemas import Todo, TodoCreate

router = APIRouter(prefix='/todos')


@router.post('', response_model=Todo, status_code=status.HTTP_201_CREATED)
def create(*, session: Session, instance: TodoCreate):
    entity = models.Todo(**instance.model_dump())

    session.add(entity)
    session.commit()
    session.refresh(entity)

    return entity


@router.get('', response_model=list[Todo], status_code=status.HTTP_200_OK)
def read(*, session: Session, skip: int = Query(None), limit: int = Query(None)):
    stmt = select(models.Todo).offset(skip).limit(limit)

    return session.scalars(stmt).all()


@router.get('/{id}', response_model=Todo, status_code=status.HTTP_200_OK)
def read_unique(*, session: Session, id: int):
    entity = session.get(models.Todo, id)

    if not entity:
        raise NotFoundException(f'{models.Todo.__name__} #{id} not found')

    return entity


@router.put('/{id}', response_model=Todo, status_code=status.HTTP_200_OK)
def update(*, session: Session, id: int, instance: TodoCreate):
    entity = session.get(models.Todo, id)

    if not entity:
        raise NotFoundException(f'{models.Todo.__name__} #{id} not found')

    for k, v in instance.model_dump(exclude_unset=True).items():
        setattr(entity, k, v)

    session.add(entity)
    session.commit()
    session.refresh(entity)

    return entity


@router.delete('/{id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete(*, session: Session, id: int):
    entity = session.get(models.Todo, id)

    if not entity:
        raise NotFoundException(f'{models.Todo.__name__} #{id} not found')

    session.delete(entity)
    session.commit()
