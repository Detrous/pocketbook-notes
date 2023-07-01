from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_utils import create_database, database_exists

DATABASE_URL = "sqlite:///exporter/pocketbook_data/books.db"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()


@contextmanager
def session_scope() -> Session:
    session: Session = SessionLocal()
    session.begin()
    try:
        yield session
        session.commit()
    except Exception as ex:  # noqa
        print(ex)
        session.rollback()
    finally:
        session.close()
