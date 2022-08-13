from fastapi import APIRouter, Depends, Path
from fastapi.responses import Response
from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from {{cookiecutter.name}}.db.models import Example
from {{cookiecutter.name}}.db import get_session


router = APIRouter(tags=["Example"])


@router.get(
    "/admin/{secret_key}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
)
async def select_handler(
    secret_key: UUID4 = Path(...),
    db: AsyncSession = Depends(get_session),
):
    query = select(Example)
    result = await db.execute(query)
    # db.commit()
