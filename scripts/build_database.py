from pathlib import Path
import sqlite3

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATABASE_DIR = PROJECT_ROOT / "database" / "sqlite"
DATABASE_FILE = DATABASE_DIR / "mizan.db"

DATABASE_DIR.mkdir(parents=True, exist_ok=True)

connection = sqlite3.connect(DATABASE_FILE)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS hadith (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kitab TEXT NOT NULL,
    nomor INTEGER NOT NULL,
    arab TEXT,
    indonesia TEXT
)
""")

connection.commit()

print("Database siap digunakan:")
print(DATABASE_FILE)

connection.close()
