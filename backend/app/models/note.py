from app.db import Base
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, relationship


class NoteModel(Base):
    __tablename__ = "notes"

    id = Column(BigInteger, primary_key=True, index=True)
    internal_id = Column(BigInteger, unique=True)
    book_id = Column(BigInteger, ForeignKey("books.id", ondelete="CASCADE"), index=True)
    book: Mapped["BookModel"] = relationship(back_populates="notes")  # noqa

    quote = Column(String, nullable=False)

    context = Column(String, nullable=True)
    language = Column(String, nullable=True)
    translation = Column(String, nullable=True)

    added_at = Column(DateTime, nullable=False)
