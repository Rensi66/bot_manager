from sqlalchemy.ext.asyncio import AsyncSession
from ..models.users import Users


async def create_user(user_name: str, user_password: str, db: AsyncSession) -> Users:
    new_user = Users(user_name=user_name, user_password=user_password)

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user