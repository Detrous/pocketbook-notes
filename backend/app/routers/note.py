from typing import List

from app.dependencies import get_service
from app.schemas.note import NoteSchema
from app.services.note import NoteService
from fastapi import APIRouter, status

router = APIRouter(tags=["notes"], prefix="/notes")


@router.get("", status_code=status.HTTP_200_OK, response_model=List[NoteSchema])
async def get_books(service: NoteService = get_service(NoteService)):
    return service.get_notes()
