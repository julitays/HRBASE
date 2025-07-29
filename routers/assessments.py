from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import Assessment, AssessmentCreate
from crud import create_assessment, get_all_assessments, get_assessments_for_employee

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Assessment)
def create_new_assessment(data: AssessmentCreate, db: Session = Depends(get_db)):
    return create_assessment(db, data)

@router.get("/", response_model=list[Assessment])
def list_assessments(db: Session = Depends(get_db)):
    return get_all_assessments(db)

@router.get("/employee/{employee_id}", response_model=list[Assessment])
def get_by_employee(employee_id: int, db: Session = Depends(get_db)):
    return get_assessments_for_employee(db, employee_id)
