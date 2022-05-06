from lib2to3.pytree import Base
from pydantic import BaseModel
from uuid import UUID

from models.accounts import User


class ToDo(BaseModel):
    _id: UUID
    name: str
    description: str
    author: User
    created_at: str
