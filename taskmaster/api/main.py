from fastapi import APIRouter

from taskmaster.api.routers import todos

router = APIRouter(prefix='/api/v0')
router.include_router(todos.router, tags=['Todo'])
