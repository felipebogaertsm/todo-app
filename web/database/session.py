from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL: str = "postgresql://db:5432/todo"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
