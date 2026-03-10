from sqlalchemy import CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Users(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_name: Mapped[str] = mapped_column(unique=True)
    user_password: Mapped[str]

    __table_args__ = (
        CheckConstraint('length(user_name) >= 4', name='min_user_name_length'),
        CheckConstraint('length(user_password) >= 8', name='min_user_passwrod_length'))