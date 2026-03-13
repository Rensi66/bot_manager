from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas.users import CreateUser, UserOut

from ..crud import users
from ..crud.database import get_db

import logging


router = APIRouter()

logger = logging.getLogger(__name__)


@router.post('/users/new_user', status_code=201, response_model=UserOut)
async def create_user(user: CreateUser, db: AsyncSession = Depends(get_db)):
    logger.info('Запрос на создание пользователя')

    try:
        new_user = await users.create_user(user_name=user.user_name, user_password=user.user_password, db=db)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return new_user


