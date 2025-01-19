from pydantic import BaseModel
from typing import Optional


class ErrorModel(BaseModel):
    errorCode: Optional[str] = None
    errorMessage: str
