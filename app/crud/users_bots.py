from sqlalchemy.ext.asyncio import AsyncSession
from ..models.users_bots import Users_Bots


async def create_user_bot(user_id: int, bot_id: int, title: str, db: AsyncSession) -> Users_Bots:
    new_user_bot = Users_Bots(u_id=user_id, b_id=bot_id, title=title)

    db.add(new_user_bot)
    await db.commit()
    await db.refresh(new_user_bot)

    return new_user_bot


