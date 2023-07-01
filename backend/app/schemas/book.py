from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    title: str
    authors: Optional[str]
    added_at: datetime

    class Config:
        orm_mode = True
