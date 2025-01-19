from pydantic import BaseModel

from src.entidades.datarespuesta_schema import DataRespuestaModel


class ApiRespuestaModel(BaseModel):
    data: DataRespuestaModel
    lastAction: str
    success: bool
    textResponse: str
    titleResponse: str

    class Config:
        orm_mode = True
        exclude_none = True