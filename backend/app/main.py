from fastapi import FastAPI, HTTPException

from .database import SessionLocal
from .models import Hadith
from .utils import hadith_to_dict
from .search import search_hadith

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
        result.append(hadith_to_dict(h))

    session.close()

    return result


@app.get("/hadiths/search")
def search(q: str):
    session = SessionLocal()

    hadiths = search_hadith(session, q)

    result = []

    for h in hadiths:
        result.append(hadith_to_dict(h))

    session.close()

    return result


@app.get("/hadiths/{hadith_id}")
def get_hadith(hadith_id: int):
    session = SessionLocal()

    hadith = session.get(Hadith, hadith_id)

    if hadith is None:
        session.close()
        raise HTTPException(status_code=404, detail="Hadith not found")

    result = hadith_to_dict(hadith)

    session.close()

    return result