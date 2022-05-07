from uuid import UUID, uuid4

from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["users"])
async def get_all_users() -> list[dict[str, str]]:
    return [{"email": "felipebogaerts@gmail.com"}]


@router.get("/{user_id}")
async def get_user_by_id(user_id: UUID) -> dict[str, str]:
    return {"id": user_id, "email": "me@felipebm.com"}


@router.post("/", tags=["users", "create"])
async def create_user(user_email: str, user_password: str) -> dict[str, str]:
    return {"id": uuid4(), "email": user_email, "password": user_password}
