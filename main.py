from src.entidades.respuesta_api_codigo_schema import ApiRespuestaCodigoModel
from src.entidades.respuesta_api_schema import ApiRespuestaModel
from src.entidades.usuario_schema import UserModel
from src.negocio.usuario import usuario
from fastapi import FastAPI, APIRouter, HTTPException

from src.negocio.utilidades.respuesta.gestor_respuesta import respuesta_ok, respuesta_error_bad_request

app = FastAPI()
base_path = APIRouter(prefix="/cripto-wallet-pairs/api/v1")

ACCION_CREAR_USUARIO: str = "Crear Usuario"
USUARIO_EXITOSO: str = "Usuario creado correctamente"
EROR_CREAR_USUARIO: str = "No se ha podido crear usuario"


from fastapi import HTTPException

@base_path.post("/usuario/crear")
async def root(usuario_model: UserModel)-> ApiRespuestaModel :
    try:
        if usuario.crear_usuario(usuario_model):
            respuesta_api: ApiRespuestaCodigoModel = respuesta_ok(usuario_model, ACCION_CREAR_USUARIO, USUARIO_EXITOSO)
            return respuesta_api.respuesta_creada
        else:
            raise respuesta_error_bad_request(ACCION_CREAR_USUARIO, EROR_CREAR_USUARIO)
    except HTTPException as http_exc:  # Manejar específicamente excepciones HTTP conocidas
        raise http_exc
    except Exception as e:  # Manejar excepciones no esperadas
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@base_path.post("/usuario/obtener")
async def root(usuario_model: UserModel):
    return usuario.buscar_usuario(usuario_model)

@base_path.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# Registramos el APIRouter en la aplicación principal
app.include_router(base_path)