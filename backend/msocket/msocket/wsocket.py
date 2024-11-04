from fastapi import APIRouter, WebSocket, Depends, Header, WebSocketException, status, WebSocketDisconnect
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated, Optional

from backend.utils.utils.log import getLogger
from backend.msocket.msocket.zclient import zhipu_client


socket_router = APIRouter()
oauth2_schema = OAuth2PasswordBearer(tokenUrl="")

async def verify_token(token: str = Depends(oauth2_schema)):
    getLogger().info(f"hits token verification: {token}")
    if token is None:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    return token

@socket_router.websocket("/zhipu")
async def connect(*, websocket: WebSocket, token: Annotated[str, Depends(verify_token)]):
    getLogger().info(f"hits zhipu ws")
    await websocket.accept()
    zsocket = await zhipu_client()
    zsocket
    try:
        while True:
            data = await websocket.receive_text()
            getLogger().info(f"received msg from client: {data}")        
            await websocket.send_text(f"received you msg: {data}")
    except WebSocketDisconnect:
        getLogger().info(f"soket connection disconnected for {token}")
        raise WebSocketDisconnect