from src.negocio.usuarios import usuarios
from src.entidades.usuario_model import User_Model

from fastapi import FastAPI

app = FastAPI()


@app.post("/")
async def root(usuario: User_Model):
    usuarios.crear_usuario(usuario)
    return usuario


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
