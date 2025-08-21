import asyncio
import websockets
import aioconsole  

async def chat_client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        # Listen for messages
        async def receive_messages():
            async for message in websocket:
                print(f"\nReceived: {message}")
        
        # Send messages
        async def send_messages():
            while True:
                message = await aioconsole.ainput("Your message: ")
                await websocket.send(message)
                if message == "unsubscribe" or message == "close":
                    await websocket.close()
                    break
        
        # Run both tasks concurrently
        await asyncio.gather(
            receive_messages(),
            send_messages()
        )

asyncio.run(chat_client())