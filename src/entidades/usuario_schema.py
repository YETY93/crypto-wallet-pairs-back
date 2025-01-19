from datetime import datetime

from pydantic import BaseModel

class UserModel(BaseModel):
    created_at: datetime | None = None
    deleted_at: datetime | None = None
    nombre_usuario: str
    password: str