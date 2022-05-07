from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["todos"])
async def read_todos() -> list[dict[str, str]]:
    return [{"name": "Wash dishes"}]
