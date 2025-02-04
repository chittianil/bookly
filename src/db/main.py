from sqlmodel import create_engine, text,SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine,AsyncSession
from src.config import Config
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from src.books.models import Book
from sqlalchemy.orm import sessionmaker

async_engine = AsyncEngine(create_engine(url=Config.DATABASE_URL))


async def initdb():
     async with async_engine.begin() as conn:
          await conn.run_sync(SQLModel.metadata.create_all)

AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)      