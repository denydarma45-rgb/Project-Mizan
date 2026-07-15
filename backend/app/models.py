from sqlalchemy import ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    slug: Mapped[str] = mapped_column(String, unique=True, index=True)

    title_ar: Mapped[str] = mapped_column(String)

    title_en: Mapped[str] = mapped_column(String)

    author_ar: Mapped[str] = mapped_column(String)

    author_en: Mapped[str] = mapped_column(String)

    total_hadith: Mapped[int] = mapped_column(Integer)

    chapters = relationship(
        "Chapter",
        back_populates="book",
        cascade="all, delete-orphan",
    )

    hadiths = relationship(
        "Hadith",
        back_populates="book",
        cascade="all, delete-orphan",
    )


class Chapter(Base):
    __tablename__ = "chapters"

    __table_args__ = (
        UniqueConstraint(
            "book_id",
            "chapter_number",
            name="uq_book_chapter_number",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id"),
        index=True,
    )

    chapter_number: Mapped[int] = mapped_column(
        Integer,
        index=True,
    )

    title_ar: Mapped[str] = mapped_column(String)

    title_en: Mapped[str] = mapped_column(String)

    book = relationship(
        "Book",
        back_populates="chapters",
    )

    hadiths = relationship(
        "Hadith",
        back_populates="chapter",
    )


class Hadith(Base):
    __tablename__ = "hadiths"

    __table_args__ = (
        UniqueConstraint(
            "book_id",
            "hadith_number",
            name="uq_book_hadith_number",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id"),
        index=True,
    )

    chapter_id: Mapped[int] = mapped_column(
        ForeignKey("chapters.id"),
        index=True,
    )

    hadith_number: Mapped[int] = mapped_column(
        Integer,
        index=True,
    )

    arabic: Mapped[str] = mapped_column(String)

    translation_id: Mapped[str] = mapped_column(String)

    book = relationship(
        "Book",
        back_populates="hadiths",
    )

    chapter = relationship(
        "Chapter",
        back_populates="hadiths",
    )