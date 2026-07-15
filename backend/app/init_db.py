from .database import Base, engine

# Import seluruh model agar SQLAlchemy mendaftarkan semuanya
from .models import Book, Chapter, Hadith


def recreate_database():
    print("🗑️  Menghapus seluruh tabel...")
    Base.metadata.drop_all(bind=engine)

    print("📦 Membuat ulang tabel...")
    Base.metadata.create_all(bind=engine)

    print("✅ Database Project Mizan berhasil dibuat ulang.")


if __name__ == "__main__":
    recreate_database()