from fastapi import HTTPException, status

class CredencialInvalidaException(HTTPException):
    def __init__(self, detalle: str = "Usuario o contraseña inválido"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detalle)
