from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NoteSchema(BaseModel):
    book_id: int
    quote: str
    book_name: str
    context: Optional[str]
    language: Optional[str]
    translation: Optional[str]
    added_at: datetime

    class Config:
        orm_mode = True
