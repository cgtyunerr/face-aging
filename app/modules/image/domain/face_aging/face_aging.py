"""Face aging base class service."""
from abc import ABC, abstractmethod
from PIL import Image


class FaceAging(ABC):
    """Face aging model.

    This class is an abstract class for face aging.

    Methods:
        age_face: Age the face in an image
    """
    @abstractmethod
    def face_aging(self, image: Image) -> Image:
        """Age the face in an image.

        Arguments:
            image: The image to age face.

        Returns:
            The aged face.
        """