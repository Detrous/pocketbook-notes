from typing import List

from app.models.book import BookModel
from fastapi import Request

from .base import BaseService


class BookService(BaseService):
    def __init__(self, request: Request) -> None:
        super().__init__(request)

    def get_books(self) -> List[BookModel]:
        return self._db_session.query(BookModel).all()
