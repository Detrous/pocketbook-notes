from app.db import Base
from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.orm import Mapped, relationship


class BookModel(Base):
    __tablename__ = "books"

    id = Column(BigInteger, primary_key=True, index=True)
    internal_id = Column(BigInteger, unique=True)
    title = Column(String, nullable=False)
    authors = Column(String, nullable=True)
    notes: Mapped[list["NoteModel"]] = relationship(back_populates="book", uselist=True)  # noqa
    added_at = Column(DateTime, nullable=False)

    @property
    def notes_count(self) -> int:
        return len(self.notes)
