from typing import List

from app.dependencies import get_service
from app.schemas.book import BookSchema
from app.services.book import BookService
from fastapi import APIRouter, status

router = APIRouter(tags=["books"], prefix="/books")


@router.get("", status_code=status.HTTP_200_OK, response_model=List[BookSchema])
async def get_books(service: BookService = get_service(BookService)):
    return service.get_books()
