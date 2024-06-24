from typing import AsyncGenerator, Annotated

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.exc import SQLAlchemyError

from fastapi import Depends, HTTPException

from backend.core.config import settings


engine = create_async_engine(str(settings.SQLALCHEMY_DATABASE_URI))


async def get_db() -> AsyncGenerator[AsyncSession, None, None]:
    async with AsyncSession(engine) as session:
        try:
            yield session
        except SQLAlchemyError as ex:
            raise HTTPException(status_code=500, detail=str(ex))


SessionConn = Annotated[AsyncSession, Depends(get_db)]
