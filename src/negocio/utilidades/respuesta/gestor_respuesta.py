from typing import Any
from fastapi import status

from src.schemas.datarespuesta_schema import DataRespuestaModel
from src.schemas.enums.estado_enum import EstadoRespuestaEnum
from src.schemas.respuesta_api_codigo_schema import ApiRespuestaCodigoModel
from src.schemas.respuesta_api_schema import ApiRespuestaModel
from src.negocio.utilidades.gestor.gestor_error import Gestor_Error


def respuesta_ok(data: Any, last_action: str, text_response: str, title_response: str = EstadoRespuestaEnum.SUCCESS,
                 status_code: int = status.HTTP_200_OK) -> ApiRespuestaCodigoModel:
    respuesta_creada: ApiRespuestaModel = ApiRespuestaModel(
        data=DataRespuestaModel(data=data),
        textResponse=text_response,
        lastAction=last_action,
        titleResponse=title_response,
        success=True
    )
    return ApiRespuestaCodigoModel(
        respuesta_creada=respuesta_creada, codigo_respuesta=status_code
    )

def _crear_respuesta_error(
    last_action: str,
    text_response: str,
    title_response: str = "FAILED",
    status_code: int = 400 ) -> ApiRespuestaCodigoModel:
    gestor_error = Gestor_Error()
    respuesta_creada: ApiRespuestaModel = ApiRespuestaModel(
        data=DataRespuestaModel(
            errores=gestor_error.obtener_errores(),
            totalErrores=gestor_error.contar_errores()
        ),
        lastAction=last_action,
        success=False,
        textResponse=text_response,
        titleResponse=title_response
    )
    return ApiRespuestaCodigoModel(
        respuesta_creada=respuesta_creada,
        codigo_respuesta=status_code
    )

def respuesta_error_bad_request(
    last_action: str,
    text_response: str,
    title_response: str = EstadoRespuestaEnum.FAILED ) -> ApiRespuestaCodigoModel:
    return _crear_respuesta_error(
        last_action, text_response, title_response, status.HTTP_400_BAD_REQUEST
    )

def respuesta_error_inautorizado(
    last_action: str,
    text_response: str,
    title_response: str = EstadoRespuestaEnum.FAILED ) -> ApiRespuestaCodigoModel:
    return _crear_respuesta_error(
        last_action, text_response, title_response, status.HTTP_401_UNAUTHORIZED
    )