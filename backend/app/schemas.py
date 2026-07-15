from pydantic import BaseModel


class HadithResponse(BaseModel):
    id: int
    hadith_number: int
    arabic: str
    translation_id: str

    class Config:
        from_attributes = True


class BookResponse(BaseModel):
    id: int
    slug: str
    title_ar: str
    title_en: str
    author_ar: str
    author_en: str
    total_hadith: int

    class Config:
        from_attributes = True