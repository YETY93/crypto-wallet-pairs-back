from src.schemas.usuario_schema import UserModel
from src.negocio.utilidades.seguridad.password import verificar_password


def validar_usuario(usuario_obtenido: UserModel, usuario_enviado: UserModel):
    if usuario_obtenido is None:
        # aaca uan excepcion que diga  usuario y contrasena invalido
        raise Exception("El usuario no se encuentra")
    if not verificar_password(usuario_enviado.password, usuario_obtenido.password):
        # en ese otra excepcion que diga suario y contrasena invalido
        return False