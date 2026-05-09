from .base import Base
from sqlalchemy.orm import Mapped

class Item(Base):
    __tablename__ = "items"

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]  