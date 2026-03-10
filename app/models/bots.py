from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Bots(Base):
    __tablename__ = 'bots'

    bot_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    bot_token: Mapped[str] = mapped_column(unique=True)
