from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    # Эта модель АБСТРАКТНАЯ
    __abstract__ = True
    
    id : Mapped[int] = mapped_column(primary_key=True)