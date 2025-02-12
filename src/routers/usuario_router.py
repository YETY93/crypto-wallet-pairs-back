from fastapi import APIRouter, HTTPException

from src.negocio.utilidades.respuesta.gestor_respuesta import respuesta_ok, respuesta_error_bad_request
from src.schemas.respuesta_api_codigo_schema import ApiRespuestaCodigoModel
from src.schemas.respuesta_api_schema import ApiRespuestaModel
from src.schemas.usuario_schema import UserModel
from src.negocio.usuario import usuario


router: APIRouter = APIRouter(prefix="/usuario", tags=["usuarios"])


ACCION_CREAR_USUARIO: str = "Crear Usuario"
USUARIO_EXITOSO: str = "Usuario creado correctamente"
EROR_CREAR_USUARIO: str = "No se ha podido crear usuario"


@router.post("/crear")
async def crear_usuario(usuario_model: UserModel)-> ApiRespuestaModel :
    try:
        respuesta_api: ApiRespuestaCodigoModel
        if usuario.crear_usuario(usuario_model):
            respuesta_api = respuesta_ok(usuario_model, ACCION_CREAR_USUARIO, USUARIO_EXITOSO)
        else:
            # TODO: Se deolveria falso si el usuario ya existe
            respuesta_api = respuesta_error_bad_request(ACCION_CREAR_USUARIO, EROR_CREAR_USUARIO)
        return respuesta_api.respuesta_creada
    except HTTPException as http_exc:  # Manejar específicamente excepciones HTTP conocidas
        raise http_exc
    except Exception as e:  # Manejar excepciones no esperadas
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")


@router.post("/usuario/obtener")
async def buscar_usuario(usuario_model: UserModel):
    return usuario.obtener_usuario(usuario_model)