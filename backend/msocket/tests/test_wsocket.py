from fastapi.testclient import TestClient
from fastapi import FastAPI
from backend.msocket.msocket.wsocket import socket_router

def test_wsocket():
    app = FastAPI()
    app.include_router(socket_router, prefix="/ws")
    client = TestClient(app)

    with client.websocket_connect("/ws/zhipu") as websocket:
        data = websocket.receive_json()
        assert data == "test"