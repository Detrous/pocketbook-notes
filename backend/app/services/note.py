from typing import List

from app.models.note import NoteModel
from fastapi import Request

from .base import BaseService


class NoteService(BaseService):
    def __init__(self, request: Request) -> None:
        super().__init__(request)

    def get_notes(self) -> List[NoteModel]:
        return self._db_session.query(NoteModel).all()
