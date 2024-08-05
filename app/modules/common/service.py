"""Common service package."""
from logging import Logger

from pydantic import BaseModel, ConfigDict


class Service(BaseModel):
    """Service class.

    The database instances are shared between its methods.

    Attributes:
        model_config: Pydantic model config.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)
