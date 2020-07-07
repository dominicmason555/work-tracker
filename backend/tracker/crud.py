from datetime import datetime

from sqlalchemy.orm import session

from . import models, schemas


def get_task(db: session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_task_notes(db: session, task_id: int):
    return db.query(models.Task.notes_path).filter(models.Task.id == task_id).first()


def get_tasks(db: session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def create_task(db: session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict(), added=datetime.now())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    db_task.notes_path = f"notes/{db_task.id}_{db_task.name.replace(' ', '_')}.md"
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: session, task_id: int, task: schemas.TaskCreate):
    updated = db.query(models.Task).filter(models.Task.id == task_id).update(task.dict())
    if (updated == 0):
        db_task = models.Task(**task.dict(), added=datetime.now())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        db_task.notes_path = f"notes/{db_task.id}_{db_task.name.replace(' ', '_')}.md"
        db.add(db_task)
        db.commit()
        return db_task
    db.commit()
    return get_task(db, task_id)


def delete_task(db: session, task_id: int):
    deleted = db.query(models.Task).filter(models.Task.id == task_id).delete()
    db.commit()
    return deleted