"""Common domain functions for image module."""
from base64 import b64decode, b64encode
import io

from PIL import Image, ImageFile
from pydantic import ConfigDict, validate_call


@validate_call(config=ConfigDict(arbitrary_types_allowed=True))
def base64_to_image(base64_str: str) -> ImageFile:
    """Convert base64 string to image.

    Arguments:
        base64_str: The base64 string.

    Returns:
        The image.
    """
    image_data = b64decode(base64_str)
    image = Image.open(io.BytesIO(image_data))
    return image


def image_to_base64(image: ImageFile) -> str:
    """Convert image to base64 string.

    Arguments:
        image: The image.

    Returns:
        The base64 string.
    """
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return b64encode(buffered.getvalue()).decode('utf-8')
