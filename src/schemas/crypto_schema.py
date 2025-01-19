from datetime import datetime, date

from pydantic import BaseModel

class CryptoModel(BaseModel):
    created_at: datetime
    deleted_at: datetime
    id_usuario: int
    nombre_cripto: str
    simbolo_cripto: str
    fecha_compra: date
    fecha_lanzamiento: date | None = None
    precio_compra: float
    cantidad: float
    precio_actual: float | None = None
    sitio_web: str
    canal_telegram: str | None = None
    id_billetera: str


