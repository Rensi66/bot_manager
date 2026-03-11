from sqlalchemy.ext.asyncio import AsyncSession
from ..models import Users

async def create_user(user_name: str, user_password: str, db: AsyncSession):
    new_user = Users(user_name=user_name, user_password=user_password)

    db.add(new_user)
    await db.commit()
    result = await db.refresh()

    return result







