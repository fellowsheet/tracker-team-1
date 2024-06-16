__all__ = ('router', )

from aiogram import Router

from .name import router as name_router
from .description import router as description_router
from .worker import router as worker_router
from .tags import router as tags_router
from .status import router as status_router
from .priority import router as priority_router
from .deadline import router as deadline_router

router = Router(name=__name__)

router.include_router(name_router)
router.include_router(description_router)
router.include_router(worker_router)
router.include_router(tags_router)
router.include_router(status_router)
router.include_router(priority_router)
router.include_router(deadline_router)