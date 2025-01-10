from src.entidades.usuario_model import User_Model
from src.datos.usuario_repository import crear

def crear_usuario(user: User_Model) -> bool:
    crear(user)
    return True