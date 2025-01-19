from src.entidades.usuario_schema import UserModel
from src.datos.usuario_repository import persistir_usuario, obtener_usuario
from src.negocio.utilidades.seguridad.password import hash_password


def crear_usuario(user: UserModel) -> bool:
    usuario: UserModel = UserModel(nombre_usuario=user.nombre_usuario, password=user.password)
    usuario.password = hash_password(user.password)
    return persistir_usuario(usuario)

def buscar_usuario(user: UserModel) -> UserModel:
    return obtener_usuario(user.nombre_usuario)

def autenticar_usuario(usuario: UserModel) -> bool:
    usuario_alamacenado: UserModel =  buscar_usuario(usuario)
    if usuario_alamacenado:
        print ("Hola")


