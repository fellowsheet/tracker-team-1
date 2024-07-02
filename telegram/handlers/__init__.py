__all__ = ('router', )

from aiogram import Router

from .default_handlers import router as default_router
from .state_handlers import router as state_router

router = Router(name=__name__)

router.include_router(default_router)
router.include_router(state_router)
