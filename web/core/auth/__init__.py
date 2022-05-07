from typing import Any

from datetime import datetime, timedelta
from passlib.context import CryptContext

import jwt

from core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(
    content: Any,
    expires_in: timedelta = None,
) -> str:
    if expires_in:
        expire = datetime.utcnow() + expires_in
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    return jwt.encode(
        payload={"exp": expire, "sub": str(content)},
        key=settings.SECRET_KEY,
        algorithm=ALGORITHM,
    )


def verify_token(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)
