from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import get_role_by_name
from openai import OpenAI
import os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

@router.post("/gpt-role")
def gpt_fetch_or_generate_role(role_name: str, db: Session = Depends(get_db)):
    role = get_role_by_name(db, role_name)

    if role:
        return {
            "status": "found",
            "message": f"Роль '{role_name}' найдена в базе данных.",
            "data": {
                "name": role.name,
                "department": role.department,
                "description": role.description,
                "version": role.version
            }
        }

    # Если не найдена — GPT предлагает сгенерировать шаблон
    prompt = f"""
    Создай краткий шаблон роли '{role_name}' для HR-платформы. 
    Укажи: цели подразделения, 3 основные функции с примерами задач, 
    4 ключевые компетенции с уровнями (1–4) и 3 KPI.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Ты HR-аналитик и бизнес-консультант"},
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "status": "not_found",
        "message": f"Роль '{role_name}' не найдена в базе. GPT предложил шаблон:",
        "gpt_suggestion": response.choices[0].message.content
    }
