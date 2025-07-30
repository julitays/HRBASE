
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 1. Укажи свои данные подключения
DATABASE_URL="postgresql://postgres.lyfqjutojeqnyvlqennc:Rootroot123!@aws-0-eu-west-1.pooler.supabase.com:5432/postgres"
# Заменить на твои реальные значения
# Пример:
# DATABASE_URL = "postgresql://postgres:1234@localhost/hr_roles"

# 2. Создаём движок SQLAlchemy
engine = create_engine(DATABASE_URL)

# 3. Создаём сессию (для работы с запросами)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Базовый класс для моделей
Base = declarative_base()

