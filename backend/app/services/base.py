from fastapi import Request
from sqlalchemy.orm import Session


class BaseService:
    _db_session: Session

    def __init__(self, request: Request) -> None:
        self._db_session = request.state.db
