from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import Log, LogCreate
from crud import create_log, get_all_logs

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Log)
def write_log(data: LogCreate, db: Session = Depends(get_db)):
    return create_log(db, data)

@router.get("/", response_model=list[Log])
def list_logs(db: Session = Depends(get_db)):
    return get_all_logs(db)
