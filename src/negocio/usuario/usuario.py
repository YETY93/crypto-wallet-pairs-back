from src.entidades.usuario_model import User_Model
from src.datos.usuario_repository import persistir_usuario
from src.negocio.utilidades.seguridad.password import hash_password


def crear_usuario(user: User_Model) -> bool:
    user.password = hash_password(user.password)
    return persistir_usuario(user)