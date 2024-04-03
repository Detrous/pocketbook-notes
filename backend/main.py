from app import app  # noqa
from app.middlewares import db  # noqa
from app.routers import book, healthcheck, note
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book.router)
app.include_router(note.router)
app.include_router(healthcheck.router)
