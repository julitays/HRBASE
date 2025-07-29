from sqlalchemy.orm import Session
from models import Role, Function, Competency, KPI
from schemas import RoleCreate
from models import Employee
from schemas import EmployeeCreate
from models import Assessment
from schemas import AssessmentCreate
from models import Log
from schemas import LogCreate


def create_role(db: Session, role_data: RoleCreate):
    role = Role(
        name=role_data.name,
        department=role_data.department,
        description=role_data.description,
        version=role_data.version
    )
    db.add(role)
    db.commit()
    db.refresh(role)

    # Добавляем функции
    for func in role_data.functions:
        db_func = Function(
            role_id=role.id,
            function_name=func.function_name,
            task_examples=func.task_examples
        )
        db.add(db_func)

    # Добавляем компетенции
    for comp in role_data.competencies:
        db_comp = Competency(
            role_id=role.id,
            name=comp.name,
            level=comp.level,
            indicators=comp.indicators
        )
        db.add(db_comp)

    # Добавляем KPI
    for kpi in role_data.kpis:
        db_kpi = KPI(
            role_id=role.id,
            metric_name=kpi.metric_name,
            frequency=kpi.frequency,
            recommendations=kpi.recommendations
        )
        db.add(db_kpi)

    db.commit()
    return role


def get_all_roles(db: Session):
    return db.query(Role).all()

def get_role_by_id(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()

def create_employee(db: Session, emp_data: EmployeeCreate):
    employee = Employee(
        full_name=emp_data.full_name,
        email=emp_data.email,
        current_role_id=emp_data.current_role_id
    )
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_all_employees(db: Session):
    return db.query(Employee).all()

def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()


def create_assessment(db: Session, data: AssessmentCreate):
    assessment = Assessment(
        employee_id=data.employee_id,
        role_id=data.role_id,
        assessed_by=data.assessed_by,
        assessment_date=data.assessment_date,
        competency_scores=data.competency_scores,
        gpt_summary=data.gpt_summary
    )
    db.add(assessment)
    db.commit()
    db.refresh(assessment)
    return assessment

def get_all_assessments(db: Session):
    return db.query(Assessment).all()

def get_assessments_for_employee(db: Session, employee_id: int):
    return db.query(Assessment).filter(Assessment.employee_id == employee_id).all()

def create_log(db: Session, log_data: LogCreate):
    log = Log(
        user_email=log_data.user_email,
        action=log_data.action,
        details=log_data.details,
        timestamp=log_data.timestamp
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

def get_all_logs(db: Session):
    return db.query(Log).order_by(Log.timestamp.desc()).all()

def get_role_by_name(db: Session, role_name: str):
    return db.query(Role).filter(Role.name.ilike(role_name)).first()
