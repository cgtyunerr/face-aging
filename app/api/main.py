"""Module to store the HTTP REST API."""


from fastapi import FastAPI, HTTPException, Request, status

from app.modules.common import InvalidInputError, UnprocessableEntityError
from app.modules.image import image_router

api = FastAPI(
    title="Face Aging HTTP API",
    responses={
        200: {
            "description": "OK",
        },
        204: {
            "description": "No content",
        },
        400: {
            "description": "Bad request",
        },
        422: {
            "description": "Unprocessable entity",
        },
    },
    swagger_ui_parameters={"persistAuthorization": True},
)


@api.exception_handler(ValueError)
async def error_handler(request: Request, error: ValueError):
    """Error handler for the ValueError exception."""
    error_to_status_code = {
        InvalidInputError: status.HTTP_400_BAD_REQUEST,
        UnprocessableEntityError: status.HTTP_422_UNPROCESSABLE_ENTITY,
    }

    raise HTTPException(
        status_code=error_to_status_code.get(type(error), 500),
        detail=str(error),
    )

api.include_router(image_router)
