import enum

from sqlalchemy import String, Integer, Column, DateTime, Enum, ForeignKey

from .database import Base


class Status(enum.Enum):
    ONGOING = 0
    COMPLETED = 1
    CANCELLED = 2


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    added = Column(DateTime, nullable=False)
    started = Column(DateTime)
    ended = Column(DateTime)
    status = Column(Enum(Status), nullable=False)
    name = Column(String, nullable=False)
    notes_path = Column(String)

    parent_id = Column(Integer, ForeignKey("tasks.id"))
