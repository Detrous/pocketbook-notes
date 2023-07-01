from app import app  # noqa
from app.middlewares import db  # noqa
from app.routers import book, healthcheck, note

app.include_router(book.router)
app.include_router(note.router)
app.include_router(healthcheck.router)
