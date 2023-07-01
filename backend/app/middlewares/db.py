from app import app
from app.db import session_scope
from fastapi import Request


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    with session_scope() as session:
        request.state.db = session
        return await call_next(request)
