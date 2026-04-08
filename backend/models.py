"""
SQLAlchemy ORM-модели для graph-абстракции: Entity + Link (связь)
"""

from __future__ import annotations

from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class Entity(Base):
    __tablename__ = "entities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    meta = Column(Text, default="{}")

    # Связи
    source_links = relationship(
        "Link",
        back_populates="source",
        foreign_keys="Link.source_id",
        cascade="all, delete-orphan",
    )
    target_links = relationship(
        "Link",
        back_populates="target",
        foreign_keys="Link.target_id",
        cascade="all, delete-orphan",
    )

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name, "meta": self.meta or "{}"}


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, autoincrement=True)
    source_id = Column(Integer, ForeignKey("entities.id"), nullable=False)
    target_id = Column(Integer, ForeignKey("entities.id"), nullable=False)
    meta = Column(Text, default="{}")

    source = relationship("Entity", foreign_keys=[source_id], back_populates="source_links")
    target = relationship("Entity", foreign_keys=[target_id], back_populates="target_links")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "source_id": self.source_id,
            "target_id": self.target_id,
            "meta": self.meta or "{}",
        }
