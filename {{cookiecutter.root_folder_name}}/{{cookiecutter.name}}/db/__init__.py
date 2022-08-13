from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from {{cookiecutter.name}}.utils import get_settings


convention = {
    "all_column_names": lambda constraint, table: "_".join(
        [str(column.name) for column in constraint.columns.values()]
    ),
    "ix": "ix__%(table_name)s__%(all_column_names)s",
    "uq": "uq__%(table_name)s__%(all_column_names)s",
    "ck": "ck__%(table_name)s__%(constraint_name)s",
    "fk": ("fk__%(table_name)s__%(all_column_names)s__" "%(referred_table_name)s"),
    "pk": "pk__%(table_name)s",
}

metadata = MetaData(naming_convention=convention)
DeclarativeBase = declarative_base(metadata=metadata)


class Database:
    def __init__(self, database_url: str, echo=False):
        self._engine = create_async_engine(database_url, echo=echo)
        self._async_session = sessionmaker(
            self._engine, class_=AsyncSession, expire_on_commit=False
        )

    async def init_models(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(DeclarativeBase.metadata.drop_all)
            await conn.run_sync(DeclarativeBase.metadata.create_all)

    # Dependency
    async def get_session(self) -> AsyncSession:
        async with self._async_session() as session:
            yield session


settings = get_settings()
db = Database(settings.database_uri, settings.DB_ECHO)
get_session = db.get_session

__all__ = [
    "DeclarativeBase",
    "db",
    "get_session"
]
