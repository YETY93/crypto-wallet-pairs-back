from pydantic import BaseModel

from src.schemas.respuesta_api_schema import ApiRespuestaModel


class ApiRespuestaCodigoModel(BaseModel):
    respuesta_creada: ApiRespuestaModel
    codigo_respuesta: int
