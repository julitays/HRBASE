from database import SessionLocal
from sqlalchemy import text

db = SessionLocal()

try:
    result = db.execute(text("SELECT 1"))
    print("Подключение к базе успешно!")
except Exception as e:
    print("Ошибка подключения:", e)
finally:
    db.close()
