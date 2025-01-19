from pydantic import BaseModel

from src.entidades.respuesta_api_schema import ApiRespuestaModel


class ApiRespuestaCodigoModel(BaseModel):
    respuesta_creada: ApiRespuestaModel
    codigo_respuesta: int
