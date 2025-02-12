from typing import List
from pydantic import BaseModel, Field

from src.schemas.error_schema import ErrorModel

class Gestor_Error(BaseModel):
    errores: List[ErrorModel] = Field(default_factory=list)

    def agregar_error(self, error: ErrorModel) -> None:
        self.errores.append(error)

    def obtener_errores(self) -> List[ErrorModel]:
        return self.errores

    def contar_errores(self) -> int:
        return len(self.errores)

# Singleton para gestionar la única instancia de Gestor_Error
# gestor_error = Gestor_Error()