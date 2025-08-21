import websockets
from .server_Observer import WebSocketObserver

class WebSocketServer:
    def __init__(self):
        self.observer = WebSocketObserver()
    
    async def handle_client(self, websocket):
        """Handle incoming WebSocket connections"""
        self.observer.subscribe(websocket)
        
        try:
            async for message in websocket:
                print(f"Received: {message}")
                if message == "close":
                    await websocket.send("Connection will be closed.")
                    await websocket.close()
                    break
                elif message == "unsubscribe":
                    self.observer.unsubscribe(websocket)
                else:
                    # Broadcast to all clients, excluding sender
                    print(f"Broadcasting message: {message}")
                    await self.observer.notify(
                        f"{message}", 
                        sender=websocket  # Broadcast to all, excluding sender
                    )
                
        except websockets.exceptions.ConnectionClosed as e:
            print(f"Connection closed: {e}")
