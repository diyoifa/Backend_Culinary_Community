from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session

from .envConfig import MYSQL_URI

print(MYSQL_URI)

engine = create_engine(MYSQL_URI, echo=True)

# meta_data = MetaData()

# conection = engine.connect()
# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


