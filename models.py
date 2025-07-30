from typing import List, Optional
from sqlalchemy import String, Text, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

# Описываем то, что есть в базе данных (каждую таблицу)
class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    department: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    version: Mapped[str] = mapped_column(String(50), default="1.0")

    functions: Mapped[List["Function"]] = relationship(back_populates="role", cascade="all, delete")
    competencies: Mapped[List["Competency"]] = relationship(back_populates="role", cascade="all, delete")
    kpis: Mapped[List["KPI"]] = relationship(back_populates="role", cascade="all, delete")

class Function(Base):
    __tablename__ = "functions"

    id: Mapped[int] = mapped_column(primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"))
    function_name: Mapped[str] = mapped_column(Text)
    task_examples: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    role: Mapped["Role"] = relationship(back_populates="functions")

class Competency(Base):
    __tablename__ = "competencies"

    id: Mapped[int] = mapped_column(primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"))
    name: Mapped[str] = mapped_column(String(255))
    level: Mapped[int] = mapped_column()  # 1-4
    indicators: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    role: Mapped["Role"] = relationship(back_populates="competencies")

class KPI(Base):
    __tablename__ = "kpis"

    id: Mapped[int] = mapped_column(primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"))
    metric_name: Mapped[str] = mapped_column(Text)
    frequency: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
recommendations: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    role: Mapped["Role"] = relationship(back_populates="kpis")

class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(255))
    email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    current_role_id: Mapped[Optional[int]] = mapped_column(ForeignKey("roles.id", ondelete="SET NULL"), nullable=True)

    current_role: Mapped[Optional["Role"]] = relationship(foreign_keys=[current_role_id])
    assessments: Mapped[List["Assessment"]] = relationship(back_populates="employee", cascade="all, delete")

from sqlalchemy.dialects.postgresql import JSONB

class Assessment(Base):
    __tablename__ = "assessments"

    id: Mapped[int] = mapped_column(primary_key=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id", ondelete="CASCADE"))
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"))
    assessed_by: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    assessment_date: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    competency_scores: Mapped[Optional[dict]] = mapped_column(JSONB, nullable=True)
    gpt_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    employee: Mapped["Employee"] = relationship(back_populates="assessments")
    role: Mapped["Role"] = relationship()

class Log(Base):
    __tablename__ = "logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    action: Mapped[str] = mapped_column(String(255))
    details: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    timestamp: Mapped[str] = mapped_column(String(100))  # Можно заменить на datetime, если нужно

