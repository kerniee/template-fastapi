from sqlalchemy import Column, text
from sqlalchemy.dialects.postgresql import INTEGER, TEXT, TIMESTAMP, UUID
from sqlalchemy.sql import func

from {{cookiecutter.name}}.db import DeclarativeBase


class Example(DeclarativeBase):
    __tablename__ = "example"

    id = Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.uuid_generate_v4(),
        unique=True,
        doc="Unique id of the string in table",
    )
