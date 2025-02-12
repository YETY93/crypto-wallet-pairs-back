from typing import Optional
from datetime import timedelta, datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError

from src.negocio.usuario import usuario
from src.negocio.utilidades.configuracion.configuracion import Configuracion
from src.schemas.token_schema import TokenData, TokenModel
from src.schemas.usuario_schema import UserModel

configuracion: Configuracion = Configuracion()

SECRET_KEY = configuracion.secret_key
ACCESS_TOKEN_EXPIRE_MINUTES = configuracion.token_expire
ALGORITHM = "HS256"
TOKEN_TYPE = "Bearer "

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/cripto-wallet-pairs/api/v1/login")


def crear_token_acceso(data: dict, expiracion_delta: Optional[timedelta] = None) :
    encriptar = data.copy()
    if expiracion_delta:
        expiracion = datetime.now() + expiracion_delta
    else:
        expiracion = datetime.now() + timedelta(minutes=15)
    encriptar.update({"exp": expiracion})
    encripta_jwt = jwt.encode(encriptar, SECRET_KEY, algorithm=ALGORITHM)
    return encripta_jwt


def generar_token(usuario_model: UserModel) -> Optional[TokenModel]:
    usuario_logueado = usuario.autenticar_usuario(usuario_model)
    if not usuario_logueado:
        return None
    expiracion_token = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token_generado = crear_token_acceso(data=generar_diccionario(usuario_logueado), expiracion_delta=expiracion_token)
    return TokenModel(access_token=token_generado, token_type=TOKEN_TYPE)


def generar_diccionario(usuario_model: UserModel)->dict:
    return {"id": usuario_model.id, "username": usuario_model.nombre_usuario}


async def validar_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_logueado: str = payload.get("username")
        if usuario_logueado is None:
            raise credentials_exception
        token_data = TokenData(username=usuario_logueado)
    except JWTError:
        raise credentials_exception
    usuario_model: UserModel =  usuario.obtener_datos_usuario(token_data.username)
    if not usuario_model:
        raise credentials_exception
    return usuario_model
