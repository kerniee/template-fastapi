from fastapi import APIRouter
from starlette import status

from {{cookiecutter.name}}.schemas.health_check import PingResponse


router = APIRouter(tags=["Health check"])


@router.get(
    "/health_check/ping",
    response_model=PingResponse,
    status_code=status.HTTP_200_OK,
)
async def health_check():
    return PingResponse()
