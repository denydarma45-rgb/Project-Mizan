import json

from .database import SessionLocal
from .models import Hadith


def import_sample_data():
    session = SessionLocal()

    with open("database/raw/sample_hadith.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        hadith = Hadith(
            book=item["book"],
            hadith_number=item["hadith_number"],
            arabic=item["arabic"],
            translation_id=item["translation_id"],
        )

        session.add(hadith)

    session.commit()
    session.close()

    print(f"✅ Berhasil mengimpor {len(data)} hadis.")


if __name__ == "__main__":
    import_sample_data()