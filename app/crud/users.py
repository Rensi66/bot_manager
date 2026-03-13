from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.users import Users

import logging


logger = logging.getLogger(__name__)


async def create_user(user_name: str, user_password: str, db: AsyncSession) -> Users:
    logger.info(f'Попытка создать нового пользователя: {user_name}')
    new_user = Users(user_name=user_name, user_password=user_password)

    try:
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
    except IntegrityError:
        logger.warning(f'Ошибка создания пользователя. Такой логин уже есть: {user_name}')
        await db.rollback()
        raise ValueError(f'Такой пользователь уже существует: {user_name}')

    logger.info(f'Новый пользователь создан: {user_name}')
    return new_user