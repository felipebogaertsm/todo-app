from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["todos"])
async def read_todos():
    return [{"name": "Wash dishes"}]
