import sys
from fastapi import FastAPI
from routers import roles, employees, assessments, logs
from dotenv import load_dotenv
import os

# перекодирование файла в UTF-8
sys.stdout.reconfigure(encoding='utf-8')

app = FastAPI(
    title="RoleMaster HR Platform",
    version="0.1",
    description="API для работы с ролями, компетенциями и оценками"
)

app.include_router(roles.router, prefix="/roles", tags=["Roles"])
app.include_router(employees.router, prefix="/employees", tags=["Employees"])
app.include_router(assessments.router, prefix="/assessments", tags=["Assessments"])
app.include_router(logs.router, prefix="/logs", tags=["Logs"])

# Подключаю ключ Open AI 29/07/2025 - 10$
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")