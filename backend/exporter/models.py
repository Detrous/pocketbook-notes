import json
from typing import List

from exporter.db import Base
from sqlalchemy import BigInteger, Column, ForeignKey, String
from sqlalchemy.orm import Mapped, relationship


class BookModel(Base):
    __tablename__ = "Books"

    # OID      INTEGER PRIMARY KEY REFERENCES Items(OID) ON DELETE CASCADE
    oid = Column("OID", BigInteger, primary_key=True, index=True)
    # Title    TEXT
    title = Column("Title", BigInteger)
    # Authors  TEXT
    authors = Column("Authors", BigInteger)
    # TimeAdd  INTEGER NOT NULL DEFAULT (0)
    time_added = Column("TimeAdd", BigInteger)
    # backref
    items: Mapped[List["ItemModel"]] = relationship(back_populates="book")


class ItemModel(Base):
    __tablename__ = "Items"

    # OID      INTEGER PRIMARY KEY
    oid = Column("OID", BigInteger, primary_key=True, index=True)
    # ParentID INTEGER REFERENCES Items(OID)
    book_id = Column("ParentID", BigInteger, ForeignKey("Books.OID", ondelete="CASCADE"), index=True)
    book: Mapped[BookModel] = relationship(back_populates="items")
    # TypeID   INTEGER NOT NULL REFERENCES TypeNames(OID)
    type_id = Column("TypeID", BigInteger)
    # State    INTEGER NOT NULL DEFAULT (0)
    state = Column("State", BigInteger)
    # TimeAlt  INTEGER NOT NULL DEFAULT (0)
    time_alt = Column("TimeAlt", BigInteger)
    # HashUUID TEXT
    uuid = Column("HashUUID", String)
    # backref
    tags: Mapped[List["TagModel"]] = relationship(back_populates="item")


class TagNameModel(Base):
    __tablename__ = "TagNames"

    # OID      INTEGER PRIMARY KEY
    oid = Column("OID", BigInteger, primary_key=True, index=True)
    # TagName  TEXT NOT NULL
    name = Column("TagName", String)
    # Opts     INTEGER NOT NULL DEFAULT (0)
    opts = Column("Opts", BigInteger)
    # backref
    tags: Mapped[List["TagModel"]] = relationship(back_populates="tag")


class TagModel(Base):
    __tablename__ = "Tags"

    # OID      INTEGER PRIMARY KEY
    oid = Column("OID", BigInteger, primary_key=True, index=True)
    # ItemID   INTEGER NOT NULL REFERENCES Items(OID) ON DELETE CASCADE
    item_id = Column("ItemID", BigInteger, ForeignKey("Items.OID", ondelete="CASCADE"), index=True)
    item: Mapped[ItemModel] = relationship(back_populates="tags")
    # TagID    INTEGER NOT NULL REFERENCES TagNames(OID)
    tag_id = Column("TagID", BigInteger, ForeignKey("TagNames.OID", ondelete="CASCADE"), index=True)
    tag: Mapped[TagNameModel] = relationship(back_populates="tags")
    # Val      TEXT
    value = Column("Val", String)
    # TimeEdt  INTEGER NOT NULL DEFAULT (0), UNIQUE(ItemID, TagID)
    edited_at = Column("TimeEdt", BigInteger)

    @property
    def value_dict(self) -> dict:
        return json.loads(self.value)

    @property
    def tag_name(self):
        return self.tag.name
