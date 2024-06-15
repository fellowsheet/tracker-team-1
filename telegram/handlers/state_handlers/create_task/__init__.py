__all__ = ('router', )

from aiogram import Router

from .name import router as name_router
from .description import router as description_router
from .responsible_person import router as responsible_person_router
from .tags import router as tags_router

router = Router(name=__name__)

router.include_router(name_router)
router.include_router(description_router)
router.include_router(responsible_person_router)
router.include_router(tags_router)