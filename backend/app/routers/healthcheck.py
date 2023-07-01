from fastapi import APIRouter, status

router = APIRouter(tags=["healthcheck"], prefix="/healthcheck")


@router.get("", status_code=status.HTTP_200_OK)
async def healthcheck():
    return
