"""
Настройка подключения к PostgreSQL через SQLAlchemy
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://symbio:symbio@localhost:5432/symbio",
)

engine = create_engine(DATABASE_URL, pool_size=5, max_overflow=10)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    """FastAPI-зависимость: предоставляет и закрывает сессию."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Создать все таблицы (для dev/CI)."""
    from .models import Base

    Base.metadata.create_all(bind=engine)
