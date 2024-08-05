"""Image factory module."""
from functools import lru_cache

from app.modules.image.src.service import FaceAgingService


class Factory:
    """Face aging factory class."""
    @staticmethod
    @lru_cache(maxsize=1)
    def create_face_aging_service() -> FaceAgingService:
        """Create face aging service."""
        return FaceAgingService()