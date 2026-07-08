from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

engine = create_async_engine("sqlite+aiosqlite:///database.db", echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=True)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

