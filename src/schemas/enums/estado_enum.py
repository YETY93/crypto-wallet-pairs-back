from enum import Enum

class EstadoRespuestaEnum(str, Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"