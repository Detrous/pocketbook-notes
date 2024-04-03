from datetime import datetime
from typing import List

from app import db as app_db
from app import models as app_models
from exporter import db as pb_db
from exporter import models as pb_models

books = []
with pb_db.session_scope() as pb_session:
    pb_books: List[pb_models.BookModel] = pb_session.query(pb_models.BookModel).all()
    for book in pb_books:
        notes = []

        for item in book.items:
            is_valid_note = False
            note = {"internal_id": item.oid}

            for tag in item.tags:
                if tag.tag_name == "bm.type" and tag.value == "bookmark":
                    break

                if tag.tag_name == "bm.book_mark" and tag.value_dict.get("displayType") == "translation":
                    note["language"] = tag.value_dict["language"]
                    note["added_at"] = datetime.fromtimestamp(tag.value_dict["created"])
                    is_valid_note = True
                elif tag.tag_name == "bm.quotation":
                    note["quote"] = tag.value_dict["text"]
                elif tag.tag_name == "bm.note":
                    note["context"] = tag.value_dict.get("context")
                    note["translation"] = tag.value_dict.get("text")
            if is_valid_note:
                notes.append(note)
                print("New note:", note["quote"])

        if notes:
            books.append(
                {
                    "internal_id": book.oid,
                    "title": book.title,
                    "authors": book.authors,
                    "added_at": datetime.fromtimestamp(book.time_added),
                    "notes": notes,
                }
            )
            print("New book:", book.title)

with app_db.session_scope() as session:
    for pb_book in books:
        pb_notes = pb_book.pop("notes")

        app_book = (
            session.query(app_models.BookModel)
            .filter(app_models.BookModel.internal_id == pb_book["internal_id"])
            .first()
        )
        if not app_book:
            app_book = app_models.BookModel(**pb_book)
            session.add(app_book)
            session.flush()

        for pb_note in pb_notes:
            app_note = (
                session.query(app_models.NoteModel)
                .filter(app_models.NoteModel.internal_id == pb_note["internal_id"])
                .first()
            )
            if not app_note:
                session.add(app_models.NoteModel(**(pb_note | {"book_id": app_book.id})))
