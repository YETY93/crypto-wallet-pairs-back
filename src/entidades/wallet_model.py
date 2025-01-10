from datetime import datetime

from pydantic import BaseModel

class Wallet_Model(BaseModel):
    created_at: datetime | None = None
    deleted_at: datetime | None = None
    nombre: str
    proveedor: str
    direccion: str
    id_usuario: int
