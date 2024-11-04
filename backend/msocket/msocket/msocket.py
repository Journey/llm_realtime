import asyncio
import os
import logging
from websockets.server import serve

logging.basicConfig(level=logging.INFO)


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():

    port_number: int = os.environ["SOCKET_PORT_NUMBER"]
    async with serve(echo, os.environ["SOCKET_ADDRESS"], port_number):
        logging.getLogger().info("start socket server")
        await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())
