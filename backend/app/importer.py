import json
from pathlib import Path

from .database import SessionLocal
from .models import Book, Chapter, Hadith


BOOKS = [
    (
        "bukhari",
        Path("database/raw/datasets/hadith-json/db/by_book/the_9_books/bukhari.json"),
    ),
    (
        "muslim",
        Path("database/raw/datasets/hadith-json/db/by_book/the_9_books/muslim.json"),
    ),
    (
        "abudawud",
        Path("database/raw/datasets/hadith-json/db/by_book/the_9_books/abudawud.json"),
    ),
    (
        "tirmidhi",
        Path("database/raw/datasets/hadith-json/db/by_book/the_9_books/tirmidhi.json"),
    ),
    (
        "nasai",
        Path("database/raw/datasets/hadith-json/db/by_book/the_9_books/nasai.json"),
    ),
    (
        "ibnmajah",
        Path("database/raw/datasets/hadith-json/db/by_book/the_9_books/ibnmajah.json"),
    ),
    (
        "malik",
        Path("database/raw/datasets/hadith-json/db/by_book/the_9_books/malik.json"),
    ),
    (
        "ahmed",
        Path("database/raw/datasets/hadith-json/db/by_book/the_9_books/ahmed.json"),
    ),
    (
        "darimi",
        Path("database/raw/datasets/hadith-json/db/by_book/the_9_books/darimi.json"),
    ),
]


def import_books():
    session = SessionLocal()

    total_imported = 0
    total_skipped = 0

    for slug, dataset_path in BOOKS:

        print(f"\n📖 Mengimpor {slug}...")

        with open(dataset_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        metadata = data["metadata"]

        book = Book(
            slug=slug,
            title_ar=metadata["arabic"]["title"],
            title_en=metadata["english"]["title"],
            author_ar=metadata["arabic"]["author"],
            author_en=metadata["english"]["author"],
            total_hadith=metadata["length"],
        )

        session.add(book)
        session.commit()
        session.refresh(book)

        chapter_map = {}

        for item in data["chapters"]:

            chapter = Chapter(
                book_id=book.id,
                chapter_number=item["id"],
                title_ar=item["arabic"],
                title_en=item["english"],
            )

            session.add(chapter)

        session.commit()

        chapters = (
            session.query(Chapter)
            .filter_by(book_id=book.id)
            .all()
        )

        for chapter in chapters:
            chapter_map[chapter.chapter_number] = chapter.id

        imported = 0
        skipped = 0

        for item in data["hadiths"]:

            exists = (
                session.query(Hadith)
                .filter_by(
                    book_id=book.id,
                    hadith_number=item["idInBook"],
                )
                .first()
            )

            if exists:
                skipped += 1
                continue

            hadith = Hadith(
                book_id=book.id,
                chapter_id=chapter_map[item["chapterId"]],
                hadith_number=item["idInBook"],
                arabic=item["arabic"],
                translation_id=item["english"]["text"],
            )

            session.add(hadith)
            imported += 1

        session.commit()

        total_imported += imported
        total_skipped += skipped

        print(f"   Imported : {imported}")
        print(f"   Skipped  : {skipped}")

    session.close()

    print("\n==========================")
    print(f"TOTAL IMPORTED : {total_imported}")
    print(f"TOTAL SKIPPED  : {total_skipped}")
    print("==========================")


if __name__ == "__main__":
    import_books()