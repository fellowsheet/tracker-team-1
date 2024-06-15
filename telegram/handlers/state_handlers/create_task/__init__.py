__all__ = ('router', )

from aiogram import Router

from .name import router as name_router
from .description import router as description_router

router = Router(name=__name__)

router.include_router(name_router)
router.include_router(description_router)