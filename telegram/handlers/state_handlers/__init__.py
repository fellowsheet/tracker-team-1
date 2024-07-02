__all__ = ('router', )

from aiogram import Router

from .create_task import router as create_task_router

router = Router(name=__name__)

router.include_router(create_task_router)