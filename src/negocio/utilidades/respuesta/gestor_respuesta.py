from src.entidades.datarespuesta_schema import DataRespuestaModel
from src.entidades.respuesta_api_codigo_schema import ApiRespuestaCodigoModel
from src.entidades.respuesta_api_schema import ApiRespuestaModel

from typing import Any

from src.negocio.utilidades.gestor.gestor_error import Gestor_Error


def respuesta_ok(data: Any, last_action: str, text_response: str, title_response: str = "SUCCESS",
                 status_code: int = 200) -> ApiRespuestaCodigoModel:
    respuesta_creada: ApiRespuestaModel = ApiRespuestaModel(
        data=DataRespuestaModel(data=data),
        textResponse=text_response,
        lastAction=last_action,
        titleResponse=title_response,
        success=True
    )
    return ApiRespuestaCodigoModel(respuesta_creada=respuesta_creada, codigo_respuesta=status_code)

def respuesta_error_bad_request(last_action: str, text_response: str,
                                title_response: str = "FAILED", status_code: int = 400) -> ApiRespuestaCodigoModel:
    gestor_error = Gestor_Error()
    respuesta_creada: ApiRespuestaModel = ApiRespuestaModel(
        data=DataRespuestaModel(errores=gestor_error.obtener_errores(), totalErrores=gestor_error.contar_errores()),
        lastAction=last_action,
        success=False,
        textResponse=text_response,
        titleResponse=title_response
    )
    return ApiRespuestaCodigoModel(respuesta_creada=respuesta_creada, codigo_respuesta=status_code)