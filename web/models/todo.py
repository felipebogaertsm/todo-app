from uuid import UUID

from sqlalchemy import Column, DateTime, ForeignKey, String

from database import Base


class ToDo(Base):
    __tablename__ = "todos"

    _id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, default="")
    status = Column(String, default="in progress")
    author = ForeignKey()
    created_at = Column(DateTime)
