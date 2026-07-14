from pydantic import BaseModel


class HadithResponse(BaseModel):
    id: int
    book: str
    hadith_number: int
    arabic: str
    translation_id: str

    model_config = {
        "from_attributes": True
    }