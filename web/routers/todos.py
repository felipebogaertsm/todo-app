from fastapi import APIRouter

router = APIRouter(prefix="/todos")


@router.get("/", tags=["todos"])
async def read_todos() -> list[dict[str, str]]:
    return [{"name": "Wash dishes"}]
