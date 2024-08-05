"""MTCNN face detection module."""
from PIL.Image import Image
from mtcnn import MTCNN
import numpy as np
from PIL import Image

from app.modules.common.exceptions import InvalidInputError
from app.modules.image.domain import base64_to_image
from .face_detection import FaceDetection


class MtcnnFaceDetection(FaceDetection):
    """MTCNN face detection class.

    This class is a concrete class for MTCNN face detection.

    Methods:
        detect_faces: Detect face in an image and crop it
    """

    def detect_faces(self, image_base64: str) -> list[Image]:
        """Detect faces in an image and crop it.

        Arguments:
            image_base64: The image to detect face with base64 format.

        Raises:
            InvalidInputError: If no face is detected.

        Returns:
            The cropped face.
        """
        image = base64_to_image(image_base64)
        image_np = np.array(image)
        detector = MTCNN()
        try:
            faces = detector.detect_faces(image_np)
        except:
            raise InvalidInputError("Invalid image.")

        if not faces:
            raise InvalidInputError("No face detected.")

        cropped_faces = []
        for face in faces:
            x, y, w, h = face["box"]
            face_image = image_np[y:y + h, x:x + w]
            face_image_pil = Image.fromarray(face_image)
            cropped_faces.append(face_image_pil)

        return cropped_faces
