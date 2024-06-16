__all__ = ('router', )

from aiogram import Router

from .name import router as name_router
from .description import router as description_router
from .responsible_person import router as responsible_person_router
from .tags import router as tags_router
from .state import router as state_router
from .priority import router as priority_router
from .deadline_date import router as deadline_date_router

router = Router(name=__name__)

router.include_router(name_router)
router.include_router(description_router)
router.include_router(responsible_person_router)
router.include_router(tags_router)
router.include_router(state_router)
router.include_router(priority_router)
router.include_router(deadline_date_router)