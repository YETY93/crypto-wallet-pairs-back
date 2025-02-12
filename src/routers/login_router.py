from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse


from src.negocio.servicios import autenticacion_servicio
from src.negocio.utilidades.respuesta.gestor_respuesta import respuesta_ok, respuesta_error_inautorizado
from src.schemas.respuesta_api_codigo_schema import ApiRespuestaCodigoModel
from src.schemas.token_schema import TokenModel
from src.schemas.usuario_schema import UserModel


router: APIRouter = APIRouter(prefix="/login", tags=["login"])

ACCION_GENERAR_TOKEN: str = "Generar Token"
TOKEN_EXITOSO: str = "Token generado correctamente"
EROR_TOKEN: str = "No se ha podido generar el token"

@router.post("/")
async def loguear_usuario(usuario_model: UserModel):
    respuesta_api: ApiRespuestaCodigoModel
    try:
        token: TokenModel = autenticacion_servicio.generar_token(usuario_model)
        if token:
             respuesta_api = respuesta_ok(token, ACCION_GENERAR_TOKEN, TOKEN_EXITOSO)
        else:
            respuesta_api = respuesta_error_inautorizado(ACCION_GENERAR_TOKEN, EROR_TOKEN)
        return JSONResponse (content=respuesta_api.respuesta_creada.model_dump(),  status_code= respuesta_api.codigo_respuesta)
    except HTTPException as http_exc:  # Manejar específicamente excepciones HTTP conocidas
        raise http_exc
    except Exception as e:  # Manejar excepciones no esperadas
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

