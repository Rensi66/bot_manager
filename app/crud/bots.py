from sqlalchemy.ext.asyncio import AsyncSession
from ..models.bots import Bots


async def create_bot(bot_token: str, db: AsyncSession) -> Bots:
    add_bot = Bots(bot_token=bot_token)

    db.add(add_bot)
    await db.commit()
    await db.refresh(add_bot)

    return add_bot