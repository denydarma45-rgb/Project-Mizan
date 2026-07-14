from sqlalchemy import or_

from .models import Hadith


def search_hadith(session, keyword: str):
    return (
        session.query(Hadith)
        .filter(
            or_(
                Hadith.translation_id.ilike(f"%{keyword}%"),
                Hadith.arabic.ilike(f"%{keyword}%"),
            )
        )
        .all()
    )