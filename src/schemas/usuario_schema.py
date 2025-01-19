from datetime import datetime

from pydantic import BaseModel

class UserModel(BaseModel):
    id: int | None = None
    created_at: datetime | None = None
    deleted_at: datetime | None = None
    nombre_usuario: str
    password: str | None

    class Config:
        orm_mode = True
        exclude_none = True