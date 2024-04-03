from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    title: str
    authors: Optional[str]
    added_at: datetime
    notes_count: int

    class Config:
        orm_mode = True
