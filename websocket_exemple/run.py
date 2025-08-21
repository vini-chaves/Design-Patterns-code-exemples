from src import *
import asyncio
import websockets


async def main():
    start_server = websockets.serve(server.handle_client, "localhost", 8765)
    async with start_server:
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    server = WebSocketServer()
    asyncio.run(main())