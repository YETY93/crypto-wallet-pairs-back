from passlib.context import CryptContext


# Crear contexto para bcrypt
password_context = CryptContext(schemes=["bcrypt"], bcrypt__rounds=12, deprecated="auto")

def hash_password(password: str) -> str:
    """Hashea una contraseña para almacenamiento."""
    try:
        return password_context.hash(password)
    except Exception as e:
        raise RuntimeError(f"Error al hashear la contraseña: {e}")

def verify_password(password_ingresado: str, password_encriptado: str) -> bool:
    """Verifica si la contraseña en texto plano coincide con el hash almacenado."""
    try:
        return password_context.verify(password_ingresado, password_encriptado)
    except ValueError:
        return False