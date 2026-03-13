from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from ..config import Config


engine = create_async_engine(Config.DATABASE, echo=True)
session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_db():
    async with session_maker() as session:
        yield session
