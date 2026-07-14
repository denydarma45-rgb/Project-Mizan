from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Hadith(Base):
    __tablename__ = "hadiths"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    book: Mapped[str] = mapped_column(String, index=True)

    hadith_number: Mapped[int] = mapped_column(Integer, index=True)

    arabic: Mapped[str] = mapped_column(String)

    translation_id: Mapped[str] = mapped_column(String)