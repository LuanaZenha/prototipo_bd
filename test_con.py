from sqlalchemy import create_engine

# URL de conexão com o banco do Kapitour
DATABASE_URL = "mysql+pymysql://fastapi:12345@localhost/kapitour_bd"

# Criação do engine
engine = create_engine(DATABASE_URL)

# Testando a conexão
try:
    with engine.connect() as conn:
        print("✅ Conexão com o banco de dados do Kapitour bem-sucedida!")
except Exception as e:
    print("❌ Erro ao conectar ao banco de dados do Kapitour:")
    print(e)