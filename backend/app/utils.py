from .models import Hadith


def hadith_to_dict(hadith: Hadith):
    return {
        "id": hadith.id,
        "book": hadith.book,
        "hadith_number": hadith.hadith_number,
        "arabic": hadith.arabic,
        "translation_id": hadith.translation_id,
    }