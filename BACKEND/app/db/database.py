from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Neyen1995@localhost:5432/evely-new-database"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Neyen1995@localhost:5432/evely-new-database"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Esto se encarga de abrir la base de datos cuando la estamos usando y de cerrarla cuando terminamos
def get_db():
    db = Sessionmaker()
    try:
        yield db
    finally:
        db.close()

try:
    with engine.connect() as connection:
        print("Conexión exitosa a la base de datos")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
