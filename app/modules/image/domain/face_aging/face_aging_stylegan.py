"""Face aging with styleGan module."""
from PIL import Image

from .face_aging import FaceAging


class FaceAgingStyleGan(FaceAging):
    """Face aging with styleGan model.

    This class is an implementation of face aging with styleGan.

    Methods:
        age_face: Age the face in an image
    """

    def face_aging(self, image: Image) -> Image:
        """Age the face in an image.

        Arguments:
            image: The image to age face.

        Returns:
            The aged face.
        """
