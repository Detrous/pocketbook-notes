from app.services.base import BaseService
from fastapi import Depends
from fastapi.requests import Request


def get_service(service_class: BaseService):
    def wrapper(request: Request) -> BaseService:
        service = service_class(request)
        return service

    return Depends(wrapper)
