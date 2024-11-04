import asyncio
import os
import logging
from websockets.sync.client import connect

logging.basicConfig(level=logging.INFO)


def hello():
    with connect(
        f"ws://{os.environ['SOCKET_ADDRESS']}:{os.environ["SOCKET_PORT_NUMBER"]}"
    ) as websocket:
        logging.getLogger().info("start client")
        websocket.send("Hello world!")
        message = websocket.recv()
        logging.getLogger().info(f"Received: {message}")


hello()
