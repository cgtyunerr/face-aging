"""Http router for image module."""

from fastapi import APIRouter

from .http import face_aging_router

image_router = APIRouter(
    prefix="/image",
)

image_router.include_router(face_aging_router)
