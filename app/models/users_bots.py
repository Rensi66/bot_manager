from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Users_Bots(Base):
    __tablename__ = 'users_bots'

    us_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    u_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    b_id: Mapped[int] = mapped_column(ForeignKey('bots.bot_id'))
    title: Mapped[str] 

    __table_args__ = (
        UniqueConstraint('u_id', 'title', name='unique_u_id_and_title'),
        UniqueConstraint('u_id', 'b_id', name='unique_u_id_and_b_id')
    )

