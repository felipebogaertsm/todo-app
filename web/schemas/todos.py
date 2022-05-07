from pydantic import BaseModel
from uuid import UUID

from models.accounts import User


class ToDo(BaseModel):
    _id: UUID
    name: str
    description: str
    status: str
    author: User
    created_at: str
