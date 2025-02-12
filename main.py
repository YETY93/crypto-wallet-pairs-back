from fastapi import FastAPI, APIRouter

from src.routers import login_router, usuario_router

PREFIX = "/cripto-wallet-pairs/api/v1"

app = FastAPI()

app.include_router(prefix=PREFIX, router=login_router.router)
app.include_router(prefix=PREFIX, router=usuario_router.router)
