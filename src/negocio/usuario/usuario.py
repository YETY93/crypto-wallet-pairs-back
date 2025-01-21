from typing import Optional

from src.schemas.usuario_schema import UserModel
from src.datos.usuario_repository import persistir_usuario, obtener_usuario
from src.negocio.utilidades.seguridad.password import hashear_password, verificar_password


def crear_usuario(user: UserModel) -> bool:
    usuario: UserModel = UserModel(nombre_usuario=user.nombre_usuario, password=user.password)
    usuario.password = hashear_password(user.password)
    return persistir_usuario(usuario)

def obtener_datos_usuario(nombre_usuario: str) -> UserModel:
    return obtener_usuario(nombre_usuario)

def autenticar_usuario(user: UserModel) -> Optional[UserModel]:
    usuario_almacenado: UserModel = obtener_datos_usuario(user.nombre_usuario)
    if usuario_almacenado and verificar_password(user.password, usuario_almacenado.password):
        return user
    return None

