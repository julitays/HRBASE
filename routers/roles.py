from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import Role, RoleCreate
from crud import create_role, get_all_roles, get_role_by_id

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Role)
def create_new_role(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role)

@router.get("/", response_model=list[Role])
def read_roles(db: Session = Depends(get_db)):
    return get_all_roles(db)

@router.get("/{role_id}", response_model=Role)
def read_role_by_id(role_id: int, db: Session = Depends(get_db)):
    role = get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Роль не найдена")
    return role
