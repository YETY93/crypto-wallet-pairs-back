from pydantic import BaseModel

from src.schemas.datarespuesta_schema import DataRespuestaModel


class ApiRespuestaModel(BaseModel):
    data: DataRespuestaModel
    lastAction: str
    success: bool
    textResponse: str
    titleResponse: str
