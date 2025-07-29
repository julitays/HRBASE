from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class FunctionBase(BaseModel):
    function_name: str
    task_examples: Optional[str] = None

class FunctionCreate(FunctionBase):
    pass

class Function(FunctionBase):
    id: int

    class Config:
        from_attributes = True

class CompetencyBase(BaseModel):
    name: str
    level: int
    indicators: Optional[str] = None

class CompetencyCreate(CompetencyBase):
    pass

class Competency(CompetencyBase):
    id: int

    class Config:
        from_attributes = True

class KPIBase(BaseModel):
    metric_name: str
    frequency: Optional[str] = None
    recommendations: Optional[str] = None

class KPICreate(KPIBase):
    pass

class KPI(KPIBase):
    id: int

    class Config:
        from_attributes = True

class RoleBase(BaseModel):
    name: str
    department: Optional[str] = None
    description: Optional[str] = None
    version: Optional[str] = "1.0"

class RoleCreate(RoleBase):
    functions: List[FunctionCreate] = []
    competencies: List[CompetencyCreate] = []
    kpis: List[KPICreate] = []

class Role(RoleBase):
    id: int
    functions: List[Function] = []
    competencies: List[Competency] = []
    kpis: List[KPI] = []

    class Config:
        from_attributes = True

class EmployeeBase(BaseModel):
    full_name: str
    email: Optional[str] = None
    current_role_id: Optional[int] = None

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True



class AssessmentBase(BaseModel):
    employee_id: int
    role_id: int
    assessed_by: Optional[str] = None
    assessment_date: Optional[str] = None
    competency_scores: Optional[dict] = None
    gpt_summary: Optional[str] = None

class AssessmentCreate(AssessmentBase):
    pass

class Assessment(AssessmentBase):
    id: int

    class Config:
        from_attributes = True

class LogBase(BaseModel):
    user_email: Optional[str] = None
    action: str
    details: Optional[str] = None
    timestamp: str

class LogCreate(LogBase):
    pass

class Log(LogBase):
    id: int

    class Config:
        from_attributes = True
