from uuid import UUID, uuid4

from fastapi import APIRouter, status, Form

router = APIRouter(prefix="/accounts")


@router.get("/users", tags=["users"])
async def get_all_users() -> list[dict[str, str]]:
    return [{"email": "felipebogaerts@gmail.com"}]


@router.get("/users/{user_id}")
async def get_user_by_id(user_id: UUID) -> dict[str, str]:
    return {"_id": user_id, "email": "me@felipebm.com"}


@router.post(
    "/users",
    tags=["users", "create"],
    status_code=status.HTTP_201_CREATED,
)
async def create_user(user_email: str, user_password: str) -> dict[str, str]:
    return {"_id": uuid4(), "email": user_email, "password": user_password}


@router.post("/users/token/obtain", tags=["users", "token", "obtain"])
async def obtain_user_token(
    email: str = Form(...),
    password: str = Form(...),
) -> dict[str, str]:
    return {"email": email, "password": password}
