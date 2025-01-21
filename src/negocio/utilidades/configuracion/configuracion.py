import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()

class Configuracion(BaseSettings):
    secret_key: str = os.getenv('SECRET_KEY')
    token_expire: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')