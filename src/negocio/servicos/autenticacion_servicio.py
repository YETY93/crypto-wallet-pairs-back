from typing import Optional
from datetime import timedelta, datetime
from fastapi import HTTPException, status
from jose import jwt

from src.negocio.usuario import usuario
from src.negocio.utilidades.configuracion.configuracion import Configuracion
from src.schemas.usuario_schema import UserModel

configuracion: Configuracion = Configuracion()

SECRET_KEY = configuracion.secret_key
ACCESS_TOKEN_EXPIRE_MINUTES = configuracion.token_expire
ALGORITHM = "HS256"

def crear_token_acceso(data: dict, expiracion_delta: Optional[timedelta] = None) :
    encriptar = data.copy()
    if expiracion_delta:
        expiracion = datetime.now() + expiracion_delta
    else:
        expiracion = datetime.now() + timedelta(minutes=15)
    encriptar.update({"exp": expiracion})
    encripta_jwt = jwt.encode(encriptar, SECRET_KEY, algorithm=ALGORITHM)
    return encripta_jwt

def generar_token(usuario_model: UserModel):
    usuario_logueado = usuario.autenticar_usuario(usuario_model)
    if not usuario_logueado:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email/username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    expiracion_token = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    usuario_diccionario: dict = generar_diccionario(usuario_logueado)
    return crear_token_acceso(data={"id": usuario_model.id, "username": usuario_model.username}, expiracion_delta=expiracion_token)

def generar_diccionario(usuario_model: UserModel)->dict:
    if usuario_model:
        return {"id": usuario_model.id, "username": usuario_model.username}