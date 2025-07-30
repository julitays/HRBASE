# init_db.py

from database import engine
from models import Base

print("Инициализация базы...")
print(engine.url)

# Создание всех таблиц в облачной базе Supabase
Base.metadata.create_all(bind=engine)

print("Таблицы должны быть созданы!")