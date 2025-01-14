from src.entidades.usuario_model import User_Model
from src.negocio.usuario import usuario
from fastapi import FastAPI, HTTPException

app = FastAPI()


from fastapi import HTTPException

@app.post("/")
async def root(usuario_model: User_Model):
    try:
        if usuario.crear_usuario(usuario_model):
            return {"message": "Usuario creado exitosamente", "usuario": usuario_model.nombre_usuario}
        else:
            raise HTTPException(status_code=400, detail="No se pudo crear el usuario.")
    except HTTPException as http_exc:  # Manejar específicamente excepciones HTTP conocidas
        raise http_exc
    except Exception as e:  # Manejar excepciones no esperadas
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
