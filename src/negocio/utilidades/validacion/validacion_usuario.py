from src.entidades.usuario_model import User_Model
from src.negocio.utilidades.seguridad.password import verify_password


def validar_usuario(usuario_obtenido: User_Model, usuario_enviado: User_Model):
    if usuario_obtenido is None:
        # aaca uan excepcion que diga  usuario y contrasena invalido
        raise Exception("El usuario no se encuentra")
    if not verify_password(usuario_enviado.password, usuario_obtenido.password):
        # en ese otra excepcion que diga suario y contrasena invalido
        return False