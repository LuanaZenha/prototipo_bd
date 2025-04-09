from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco de dados do Kapitour
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://fastapi:12345@localhost/kapitour_bd"

# Criação do engine SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos
Base = declarative_base()

# Dependência para obter uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


