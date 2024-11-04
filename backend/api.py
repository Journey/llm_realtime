from backend.auth.auth.auth import generate_token
from backend.auth.auth.api import auth_router
from backend.msocket.msocket.wsocket import socket_router
from fastapi import FastAPI

app = FastAPI()
# app.add_middleware()


@app.get("/", response_model=str)
async def status():
    return "it works!"

app.include_router(auth_router, prefix="/auth")
app.include_router(socket_router, prefix="/ws")
