"""Face detection base class service."""
from abc import ABC, abstractmethod


class FaceDetection(ABC):
    """Face detection model.

    This class is an abstract class for face detection.

    Methods:
        detect_faces: Detect face in an image and crop it
    """
    @abstractmethod
    def detect_faces(self, image: str) -> str:
        """Detect face in an image and crop it.

        Arguments:
            image: The image to detect face.

        Raises:
            NorFoundError: If no face is detected.

        Returns:
            The cropped face.
        """

