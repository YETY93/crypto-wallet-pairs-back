from src.entidades.usuario_model import User_Model
from src.datos.usuario_repository import persistir_usuario, obtener_usuario
from src.negocio.utilidades.seguridad.password import hash_password


def crear_usuario(user: User_Model) -> bool:
    user.password = hash_password(user.password)
    return persistir_usuario(user)

def buscar_usuario(user: User_Model) -> User_Model:
    return obtener_usuario(user.nombre_usuario)

def autenticar_usuario(usuario: User_Model) -> bool:
    usuario_alamacenado: User_Model =  buscar_usuario(usuario)
    if usuario_alamacenado:

