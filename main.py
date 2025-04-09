from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from rotas import usuario

app = FastAPI()

# CORS - permite o frontend se comunicar com o backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5178"],  # frontend React (Vite)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)

# Inclusão das rotas de usuário
app.include_router(usuario.router)

# Endpoint de teste
@app.get("/")
def read_root():
    return {"mensagem": "API do Kapitour está no ar 💪🏾"}






