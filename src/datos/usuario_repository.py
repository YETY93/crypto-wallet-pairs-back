from src.datos.db_conector import ejecutar_sentencia

from src.entidades.usuario_model import User_Model


def crear(usuario: User_Model):
    query = "INSERT INTO crypto_wallet.users (user_name, user_password) VALUES (%s, %s)"
    valores = (usuario.nombre_usuario, usuario.password)
    return ejecutar_sentencia(query, valores)