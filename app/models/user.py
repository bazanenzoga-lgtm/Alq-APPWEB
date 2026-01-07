from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Integer, String, Boolean
from app.db.session import Base 

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column (Integer, primary_key=True, index=True)  # PK
    full_name: Mapped[str] = mapped_column (String, nullable=False)
    email: Mapped[str] = mapped_column (String, unique=True, index=True, nullable=False)
    phone: Mapped[str] = mapped_column (String, nullable=True)
    password: Mapped[str] = mapped_column (String, nullable=False)
    is_owner: Mapped [bool] = mapped_column (Boolean, default=False)

