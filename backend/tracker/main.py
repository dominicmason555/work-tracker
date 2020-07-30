import os
import time
import logging
from typing import List

import colorama
import coloredlogs
import aiofiles
from aiofiles.os import remove as aio_remove
from fastapi import Depends, FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

colorama.init()
coloredlogs.install(level='INFO')

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://suse-laptop:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    logging.info("Creating task")
    return crud.create_task(db=db, task=task)


@app.put("/tasks/{task_id}/", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    logging.info(f"Updating task {task_id}")
    return crud.update_task(db=db, task_id=task_id, task=task)


@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logging.info("Retrieving tasks")
    return crud.get_tasks(db, skip=skip, limit=limit)


@app.get("/tasks/{task_id}/", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    logging.info(f"Retrieving task {task_id}")
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        logging.info(f"Task {task_id} not found")
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@app.get("/tasks/{task_id}/notes/")
async def read_task_notes(task_id: int, db: Session = Depends(get_db)):
    logging.info(f"Retrieving task {task_id}'s notes")
    db_notes = crud.get_task_notes(db, task_id=task_id)
    if db_notes is None:
        logging.info(f"Task {task_id}'s notes not in database")
        raise HTTPException(status_code=404, detail="Task notes not in database")
    elif not os.path.isfile(db_notes[0]):
        logging.info(f"Task {task_id}'s notes not in filesystem")
        raise HTTPException(status_code=404, detail="Task notes not in filesystem")
    else:
        try:
            return FileResponse(db_notes[0], filename=db_notes[0])
        except ConnectionAbortedError:
            logging.info("Client disconnected during notes reading")


@app.put("/tasks/{task_id}/notes/")
async def write_notes(task_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    logging.info(f"Writing task {task_id}'s notes")
    db_notes = crud.get_task_notes(db, task_id=task_id)
    if db_notes is None:
        logging.info(f"Task {task_id}'s notes not in database")
        raise HTTPException(status_code=404, detail="Task notes not in database")
    else:
        if not os.path.isfile(db_notes[0]):
            logging.info(f"Creating task {task_id}'s notes")
        start = time.time()
        async with aiofiles.open(db_notes[0], "w") as notes:
            contents = await file.read()
            if type(contents) != bytes:
                logging.info("Task notes not in correct format")
                raise HTTPException(status_code=422, detail="Task notes not in correct format")
            await notes.write(contents.decode("utf-8"))
        logging.info(f"File written in {time.time() - start:.3} seconds")
        return {"filename": file.filename}


@app.delete("/tasks/{task_id}/")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_notes = crud.get_task_notes(db, task_id=task_id)
    if db_notes is not None and os.path.isfile(db_notes[0]):
        await aio_remove(db_notes[0])
    return crud.delete_task(db, task_id=task_id)
