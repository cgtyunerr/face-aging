"""Face aging service module."""
from pydantic import validate_call

from app.modules.common import (
    Service,
    InvalidInputError,
)
from app.modules.image.domain import FaceDetection, MtcnnFaceDetection, image_to_base64
from app.modules.image.models import FaceAgingResponseModel

face_detection: FaceDetection = MtcnnFaceDetection()


class FaceAgingService(Service):
    """Face aging service class."""

    @validate_call
    async def age_face(self, image: str) -> FaceAgingResponseModel:
        """Age a face.

        Arguments:
            image: The image to process.

        Returns:
            FaceAgingResponseModel

        Raise:
            InvalidInputError: If the face does not detected in the image.
        """
        faces = face_detection.detect_faces(image)
        if not faces:
            raise InvalidInputError("No face detected.")

        return FaceAgingResponseModel(
            image=image_to_base64(faces[0])
        )