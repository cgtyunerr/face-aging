"""Models for face aging module."""

from pydantic import BaseModel


class FaceAgingCreateModel(BaseModel):
    """Face aging create model.

    Attributes:
        image: base64.
    """
    image: bytes


class FaceAgingResponseModel(BaseModel):
    """Face aging response model.

    Attributes:
        image: base64.
    """

    image: str
