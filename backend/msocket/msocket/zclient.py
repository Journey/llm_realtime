import asyncio
import os
import logging
from websockets.sync.client import connect, ClientConnection

logging.basicConfig(level=logging.INFO)


async def zhipu_client() -> ClientConnection:
    ws = await connect(
        f"ws://{os.environ['SOCKET_ADDRESS']}:{os.environ["SOCKET_PORT_NUMBER"]}"
    )
    return ws