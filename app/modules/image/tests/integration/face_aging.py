"""Integration tests for the face aging service."""
import pytest

from app.modules.image.tests.setup import (
    sneijder_base64,
    noface_base64,
)
from app.modules.image.src.service.face_aging import FaceAgingService


@pytest.fixture
def face_aging_service() -> FaceAgingService:
    """Create and return a face aging service instance."""
    return FaceAgingService()


class TestFaceAging:
    async def test_face_detection(self, face_aging_service):
        # Test code here
        await face_aging_service.age_face(image=sneijder_base64)
