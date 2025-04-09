from sqlalchemy import inspect
from database import Base, engine
from esquemas.usuario import Usuario

DATABASE_URL = "mysql+pymysql://fastapi:12345@localhost/kapitour_bd"

# Mostra as tabelas definidas no SQLAlchemy (via modelos)
print("Tabelas declaradas via SQLAlchemy:", list(Base.metadata.tables.keys()))

# Cria um inspetor para verificar tabelas já existentes no banco
inspector = inspect(engine)
print("Tabelas já existentes no banco de dados:", inspector.get_table_names())

# Cria todas as tabelas que ainda não existem no banco de dados
Base.metadata.create_all(bind=engine)

print("Criação de tabelas finalizada com sucesso.")

