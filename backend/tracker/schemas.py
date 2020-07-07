from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .models import Status


class TaskBase(BaseModel):
    started: Optional[datetime]
    ended: Optional[datetime]
    status: Status
    name: str
    parent_id: Optional[int]


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    added: datetime
    notes_path: str

    class Config:
        orm_mode = True
