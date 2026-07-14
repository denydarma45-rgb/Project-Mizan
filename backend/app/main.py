from fastapi import FastAPI, HTTPException

from .database import SessionLocal
from .models import Hadith
from .schemas import HadithResponse
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


@app.get("/hadiths", response_model=list[HadithResponse])
def get_hadiths():
    session = SessionLocal()

    hadiths = session.query(Hadith).all()

    session.close()

    return hadiths


@app.get("/hadiths/search", response_model=list[HadithResponse])
def search(q: str):
    session = SessionLocal()

    hadiths = search_hadith(session, q)

    session.close()

    return hadiths


@app.get("/hadiths/{hadith_id}", response_model=HadithResponse)
def get_hadith(hadith_id: int):
    session = SessionLocal()

    hadith = session.get(Hadith, hadith_id)

    if hadith is None:
        session.close()
        raise HTTPException(status_code=404, detail="Hadith not found")

    session.close()

    return hadith