from fastapi import FastAPI

from .database import SessionLocal
from .models import Hadith

app = FastAPI(
    title="Project Mizan API",
    description="API untuk pencarian, verifikasi, dan eksplorasi hadis.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Project Mizan API",
        "project": "Project Mizan",
        "version": "0.1.0",
        "status": "development",
    }


@app.get("/hadiths")
def get_hadiths():
    session = SessionLocal()

    hadiths = session.query(Hadith).all()

    result = []

    for h in hadiths:
        result.append(
            {
                "id": h.id,
                "book": h.book,
                "hadith_number": h.hadith_number,
                "arabic": h.arabic,
                "translation_id": h.translation_id,
            }
        )

    session.close()

    return result