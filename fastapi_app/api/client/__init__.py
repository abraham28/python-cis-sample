# fastapi_app/api/__init__.py
from fastapi import APIRouter

from . import create, read, update, delete

router = APIRouter()

router.include_router(create.router)
router.include_router(read.router)
router.include_router(update.router)
router.include_router(delete.router)
