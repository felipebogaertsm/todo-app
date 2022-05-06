from pydantic import BaseModel, Field
from uuid import UUID

from models.accounts import User


class ToDo(BaseModel):
    _id: UUID
    name: str = Field(min_length=1)
    description: str = Field(max_length=1e3)
    author: User
    created_at: str
