"""HTTP router fpr the image operations."""

from fastapi import APIRouter, Depends, status, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse

from app.modules.image.models import FaceAgingResponseModel, FaceAgingCreateModel
from app.modules.image.src.factory import Factory
from app.modules.image.src.service import FaceAgingService

face_aging_router: APIRouter = APIRouter(
    tags=["face-aging"],
    prefix="/face-aging",
)

face_aging_factory: FaceAgingService = Factory.create_face_aging_service()


@face_aging_router.post(
    path="/",
    summary="Create four type of aging face.",
    status_code=status.HTTP_201_CREATED,
    response_model=FaceAgingResponseModel,
)
async def face_aging(
    face_aging_create_model: FaceAgingCreateModel = Body(...),
) -> ORJSONResponse:
    """Create four type of aging face."""
    result: FaceAgingResponseModel = await face_aging_factory.age_face(
        image=face_aging_create_model.image,
    )
    return ORJSONResponse(
        content=jsonable_encoder(result),
    )
