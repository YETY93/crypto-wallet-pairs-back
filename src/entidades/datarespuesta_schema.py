from pydantic import BaseModel
from typing import Any, List, Optional, Dict

from src.entidades.error_eschema import ErrorModel


class DataRespuestaModel(BaseModel):
    data: Optional[Any] = None
    errores: Optional[List[ErrorModel]] = None
    totalErrores: Optional[int] = None

    class Config:
        exclude_none = True