from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Base


class Cats(Base):
    __tablename__ = "cats"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    breed: Mapped[str]
    age: Mapped[int]
    color: Mapped[str]
    description: Mapped[str]