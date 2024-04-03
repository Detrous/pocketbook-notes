from typing import List, Optional

from app.models.note import NoteModel
from fastapi import Request

from .base import BaseService


class NoteService(BaseService):
    def __init__(self, request: Request) -> None:
        super().__init__(request)

    def get_notes(self, query: str, book_id: Optional[int]) -> List[NoteModel]:
        query = self._db_session.query(NoteModel).filter(NoteModel.quote.ilike(f"%{query}%"))
        if book_id:
            query = query.filter(NoteModel.book_id == book_id)
        return query.all()
