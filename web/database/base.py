from uuid import UUID

from sqlalchemy.ext.declarative import declared_attr, as_declarative


@as_declarative()
class Base:
    _id: UUID
    __name__: str

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()
