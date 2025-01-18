from src.datos.db_conector import insertar_datos, obtener_dato_unico

from src.entidades.usuario_model import User_Model


def persistir_usuario(usuario: User_Model) -> bool:
    query = "INSERT INTO crypto_wallet.users (user_name, user_password) VALUES (%s, %s)"
    valores = (usuario.nombre_usuario, usuario.password)
    return insertar_datos(query, valores)

def obtener_usuario(alias_usuario: str) -> User_Model | None:
    query: str = "SELECT u.user_name, u.user_password FROM crypto_wallet.users u WHERE u.user_name = %s"
    valor: tuple = (alias_usuario,)
    valor_obtenido: tuple = obtener_dato_unico(query, valor)
    if valor_obtenido:
        return User_Model(nombre_usuario=valor_obtenido[0], password=valor_obtenido[1])
    return None